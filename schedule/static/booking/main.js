$(document).ready(function () {
    const parentEl = $(".list-of-schedules");
    const schedules = getSchedules();
    console.log(schedules)
    reloadListOfSchedule(schedules, parentEl);
})

function getSchedules(script_id='available-bookings'){
    const availBookings = load_json_data_from_script_tag(script_id);
    const convertedAvailBookings = [];

    for (const availBooking of availBookings) {
        let start = new Date(availBooking.datetime_range.start_date_time);
        let end = new Date(availBooking.datetime_range.end_date_time);
        const startSplitted = splitDateTime(start);
        const endSplitted = splitDateTime(end);

        console.assert(startSplitted.date.valueOf() === endSplitted.date.valueOf());
        convertedAvailBookings.push({
            schedule: new Schedule(startSplitted.date, startSplitted.time, endSplitted.time),
            start: start,
            end: end,
        });
    }

    return convertedAvailBookings;
}


/**
 * @param availBookings
 * @param parentElement
 */
function reloadListOfSchedule(availBookings, parentElement){
    console.log("reloaded");
    availBookings = availBookings.sort((a, b) => SCHEDULE_SORT(a.schedule, b.schedule))
    parentElement = $(parentElement);
    parentElement.empty();

    let index = 0;
    for (const availBooking of availBookings) {
        const schedule = availBooking.schedule;
        const date = dateObjToDateStringFormat(schedule.date);
        const startTime = schedule.startTime.toString();
        const endTime = schedule.endTime.toString();

        const newEl = initializeScheduleItem(date, startTime, endTime);
        newEl.click(((availBooking) =>
            (e) => {
                console.log("clicked");
                showModal(date, `${startTime} - ${endTime}`);

                const submitBtn = $("#submit-modal-btn");
                submitBtn.unbind();
                submitBtn.click(() => {
                    submitModal(availBooking.start, availBooking.end);
                });
            }
        )(availBooking));
        parentElement.append(newEl);
        index++;
    }
}


function showModal(date, timeRepr){
    const el = $('#my-modal');
    el.css('display', 'grid');
    const book_btn = el.find('#submit-modal-btn');
    book_btn.html("Book");

    el.find('.date-repr').html(date)
    el.find('.time-repr').html(timeRepr)
}
function hideModal(){
    $('#my-modal').css('display', 'none');
}
function submitModal(startDateObj, endDateObj){
    const el = $('#my-modal');
    const booker_name = el.find('#booker-name').val();

    if (booker_name.length === 0){
        alert("Please enter your name")
        return;
    }

    const book_btn = el.find('#submit-modal-btn');
    book_btn.html("Booking");

    $.post(window.location, {
        data: JSON.stringify({
            start: startDateObj,
            end: endDateObj,
            name: booker_name,
        })
    }, function (data) {
        console.assert(data.success === 1);
        window.location.reload();
    }).fail((e) => {
        alert("Booking failed!");
        console.log(e);
    });
}




function splitDateTime(date) {
    return {
        date: dateTruncateToPrevMidnight(date),
        time: Time.fromDateObj(date)
    };
}


