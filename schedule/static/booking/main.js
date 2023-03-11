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
        start = splitDateTime(start);
        end = splitDateTime(end);

        console.assert(start.date.valueOf() === end.date.valueOf());
        convertedAvailBookings.push(
            new Schedule(start.date, start.time, end.time)
        );
    }

    return convertedAvailBookings;
}


/**
 * @param {Schedule[]} availBookings
 * @param parentElement
 */
function reloadListOfSchedule(availBookings, parentElement){
    console.log("reloaded");
    availBookings = availBookings.sort(SCHEDULE_SORT)
    parentElement = $(parentElement);
    parentElement.empty();

    let index = 0;
    for (const schedule of availBookings) {
        const date = dateObjToDateStringFormat(schedule.date);
        const startTime = schedule.startTime.toString();
        const endTime = schedule.endTime.toString();

        const newEl = initializeScheduleItem(date, startTime, endTime);
        parentElement.append(newEl);
        index++;
    }
}




function splitDateTime(date) {
    return {
        date: dateTruncateToPrevMidnight(date),
        time: Time.fromDateObj(date)
    };
}


