class Schedule{
    date;
    startTime;
    endTime;

    /**
     * @param {Date} date
     * @param {Time} startTime
     * @param {Time} endTime
     */
    constructor(date, startTime, endTime) {
        dateTruncateToPrevMidnight(date);
        this.date = date;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    valueOf(){
        return this.valueOfStartime();
    }

    valueOfStartime(){
        const numOfMsSinceEpoch = this.date.valueOf();
        const numOfMsSinceMidnight = this.startTime.valueOf() * 1000;
        return numOfMsSinceEpoch + numOfMsSinceMidnight;
    }

    valueOfEndTime(){
        const numOfMsSinceEpoch = this.date.valueOf();
        const numOfMsSinceMidnight = this.endTime.valueOf() * 1000;
        return numOfMsSinceEpoch + numOfMsSinceMidnight;
    }
}

function dateObjToDateStringFormat(dateobj) {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["Jan", "Feb", "March", "April", "May", "June",
                    "July", "Aug", "Sept", "Oct", "Nov", "Dec"];

    const day = dateobj.getDay();
    const dayName = days[day]
    const date = dateobj.getDate();
    let datePrefixed = date.toString();
    if (datePrefixed.length < 2)
        datePrefixed = '0' + datePrefixed;

    const month = dateobj.getMonth();
    const year = dateobj.getFullYear();
    const monthName = months[month];

    return `${dayName}, ${datePrefixed} ${monthName} ${year}`
}


class Time{
    hour;
    minute;
    constructor(hour, minute) {
        this.hour = hour;
        this.minute = minute;
    }

    valueOf(){
        return this.hour*60 + this.minute;
    }

    toString(){
        let hour = this.hour.toString();
        const prefixedHour = (hour.length === 1)? '0'+hour: hour;
        let minute = this.minute.toString();
        const prefixedMinute = (minute.length === 1)? '0'+minute: minute;

        return `${prefixedHour}:${prefixedMinute}`;
    }
}


function getDataFromTimePicker(timePickerElement){
    let selector = "input";
    const inputEl = $(timePickerElement).find(selector).addBack(selector);
    const text = inputEl.val();

    const hourMinute = text.split(":");
    const hour  = parseInt(hourMinute[0]);
    const minute  = parseInt(hourMinute[1]);

    return new Time(hour, minute);
}

function getDateObjFromDatePicker(datePickerElement){
    let selector = "input";
    const inputEl = $(datePickerElement).find(selector).addBack(selector);
    const text = inputEl.val();

    const splittedDateFormat = text.split("/");
    const day = parseInt(splittedDateFormat[0]);
    const month = parseInt(splittedDateFormat[1])-1;  // Date() month starts from 0
    const year = parseInt(splittedDateFormat[2]);

    const date = new Date();
    date.setDate(day);
    date.setMonth(month);
    date.setFullYear(year);
    dateTruncateToPrevMidnight(date);
    return date;
}


function dateTruncateToPrevMidnight(date){
    date.setHours(0);
    date.setMinutes(0);
    date.setSeconds(0);
    date.setMilliseconds(0);
}