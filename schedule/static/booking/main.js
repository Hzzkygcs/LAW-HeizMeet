function getSchedules(){
    let availBookings = load_json_data_from_script_tag('available-bookings');

}


/**
 * @param {Schedule[]} schedules
 * @param parentElement
 */
function reloadListOfSchedule(schedules, parentElement){
    console.log("reloaded");
    schedules = schedules.sort(SCHEDULE_SORT)
    parentElement = $(parentElement);
    parentElement.empty();

    let index = 0;
    for (const schedule of schedules) {
        const date = dateObjToDateStringFormat(schedule.date);
        const startTime = schedule.startTime.toString();
        const endTime = schedule.endTime.toString();

        const newEl = initializeScheduleItem(date, startTime, endTime);
        newEl.find('.delete-btn').click(((ind) => () => {
            schedules.splice(ind, 1);
            reloadListOfSchedule(schedules, parentElement);
        })(index));

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


