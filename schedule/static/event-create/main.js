const SCHEDULE_SORT = (a, b) => a.compare(b);
let schedules = [
    new Schedule(new Date(), new Time(10, 11), new Time(12, 13)),
    new Schedule(new Date(), new Time(14, 11), new Time(19, 13)),
    new Schedule(new Date(), new Time(12, 13), new Time(12, 14)),
    new Schedule(new Date(), new Time(12, 13), new Time(12, 13)),
];


const DATE_EL = "#schedule-date";
const START_TIME_EL = "#start-time";
const END_TIME_EL = "#end-time";
const LIST_OF_SCHEDULES_EL = ".list-of-schedules";

const eventCreateInputModal = {};




function showModal(){
    $('#authentication-modal').css('display', 'grid');
    if ($(DATE_EL).val() === '')
        setToToday($(DATE_EL), 0);
    if ($(START_TIME_EL).val() === '')
        setToThisTime($(START_TIME_EL), 30*60*1000);
    if ($(END_TIME_EL).val() === '')
        setToThisTime($(END_TIME_EL), 60*60*1000);
}

function setToToday(el, addMiliSecond){
    console.log("today")
    addMiliSecond += 7 * 60 * 60 * 1000;  // UTF+7

    let dateObj = new Date();
    dateObj = new Date(dateObj.getTime() + addMiliSecond);
    const date = dateObj.getDate();
    const month = dateObj.getMonth();
    const year = dateObj.getFullYear();

    const text = `${date}/${month}/${year}`;
    console.log(text);
    $(el).val(text);
}
function setToThisTime(el, addMiliSecond){
    addMiliSecond += 7 * 60 * 60 * 1000;  // UTF+7

    let dateObj = new Date();
    dateObj = new Date(dateObj.getTime() + addMiliSecond);
    const hour = dateObj.getHours();
    const minutes = dateObj.getMinutes();

    $(el).val(`${hour}:${minutes}`);
}


function hideModal(){
    $('#authentication-modal').css('display', 'none');
}

function getScheduleObjFromModalInput(){
    let date = getDateObjFromDatePicker($(DATE_EL))
    let start = getDataFromTimePicker($(START_TIME_EL));
    let end = getDataFromTimePicker($(END_TIME_EL));

    if (start > end){
        alert("Start time cannot be greater than the end time");
        return null;
    }
    return new Schedule(date, start, end);
}

function submitModal(){
    let schedulesCopy = schedules.slice();

    const schedule = getScheduleObjFromModalInput();
    if (schedule == null)  // validation failed
        return;

    schedulesCopy.push(schedule);
    schedulesCopy = schedulesCopy.sort(SCHEDULE_SORT);

    if (!noOverlappingSchedule(schedulesCopy)) {
        console.log("Overlap");
        alert("This schedule overlaps another schedule");
        return;
    }

    schedules = schedulesCopy;
    hideModal();
    reloadListOfSchedule(schedules, $(LIST_OF_SCHEDULES_EL))
}



$(document).ready(() => {
    reloadListOfSchedule(schedules, $(LIST_OF_SCHEDULES_EL));
});

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
        console.log(schedule);
        const newEl = $($("#schedule-item-template").html());

        const date = dateObjToDateStringFormat(schedule.date);
        const startTime = schedule.startTime.toString();
        const endTime = schedule.endTime.toString();

        newEl.find(".date").text(date);
        newEl.find(".start-time").text(startTime);
        newEl.find(".end-time").text(endTime);
        newEl.find('.delete-btn').click(((ind) => () => {
            schedules.splice(ind, 1);
            reloadListOfSchedule(schedules, parentElement);
        })(index));

        parentElement.append(newEl);
        index++;
    }
}


/**
 * @param {Schedule[]} schedules
 * @returns {boolean}
 */
function noOverlappingSchedule(schedules){
    schedules = schedules.sort(SCHEDULE_SORT);

    for (let i = 0; i < schedules.length - 1; i++) {
        const curr = schedules[i];
        const next = schedules[i+1];
        const currEnd = curr.valueOfEndTime();
        const nextStart = next.valueOfStartime();
        if (currEnd > nextStart) {
            console.log(curr);
            console.log(next);
            return false;
        }
    }
    return true
}