let schedules = [];


const DATE_EL = "#schedule-date";
const START_TIME_EL = "#start-time";
const END_TIME_EL = "#end-time";




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
    let date = getDateObjFromDatePicker()
    let start = getDataFromTimePicker($(START_TIME_EL));
    let end = getDataFromTimePicker($(END_TIME_EL));

    if (start > end){
        alert("Start time cannot be greater than the end time");
        return;
    }
    return new Schedule(date, start, end);
}

function submitModal(){
    let schedulesCopy = schedules.slice();

    const schedule = getScheduleObjFromModalInput();
    schedulesCopy.push(schedule);
    schedulesCopy = schedulesCopy.sort();

    if (!noOverlappingSchedule(schedulesCopy)) {
        console.log("Overlap");
        alert("This schedule overlaps another schedule");
        return;
    }

    schedules = schedulesCopy;
    hideModal();
}





function noOverlappingSchedule(schedules){
    schedules = schedules.sort((a, b) => a.start - b.start);

    for (let i = 0; i < schedules.length - 1; i++) {
        const curr = schedules[i];
        const next = schedules[i+1];
        if (curr.end > next.start) {
            console.log(curr);
            console.log(next);
            return false;
        }
    }
    return true
}