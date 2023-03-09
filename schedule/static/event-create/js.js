let schedules = [];


const START_DATE_EL = "#start-date";
const END_DATE_EL = "#end-date";


function setToToday(el, addMiliSecond){
    addMiliSecond += 7 * 60 * 60 * 1000;  // UTF+7

    let date = new Date();
    date = new Date(date.getTime() + addMiliSecond);

    $(el).val(date.toJSON().slice(0,19));
}

function showModal(){
    if ($(START_DATE_EL).val() === '')
        setToToday($(START_DATE_EL), 0);
    if ($(END_DATE_EL).val() === '')
        setToToday($(END_DATE_EL), 30*60*1000);
    $('#authentication-modal').css('display', 'grid');
}

function hideModal(){
    $('#authentication-modal').css('display', 'none');
}

function submitModal(){
    let start = $(START_DATE_EL).val();
    let end = $(END_DATE_EL).val();
    start = new Date(start);
    end = new Date(end);
    if (start > end){
        alert("Start time cannot be greater than the end time");
        return;
    }

    let schedulesCopy = schedules.slice();

    schedulesCopy.push({
        start: start,
        end: end,
    });
    schedulesCopy = schedulesCopy.sort((a, b) => a.start - b.start);
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