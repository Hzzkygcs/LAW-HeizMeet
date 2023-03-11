function initializeScheduleItem(date, startTime, endTime) {
    const newEl = $($("#item-template").html());

    newEl.find(".date").text(date);
    newEl.find(".start-time").text(startTime);
    newEl.find(".end-time").text(endTime);

    return newEl;
}


function load_json_data_from_script_tag(script_id){
    return JSON.parse(document.getElementById(script_id).textContent)
}