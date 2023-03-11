function reload(eventsData, parentEl){
    console.log("reload")
    parentEl = $(parentEl);
    const eventItemTemplate = $("#event-item-template");

    for (const event of eventsData) {
        const newEl = $(eventItemTemplate.html());
        const {name, id} = event;
        newEl.find(".event-name").text(name);
        parentEl.append(newEl);
    }
}

$(document).ready((e) => {
    let eventsData = JSON.parse(document.getElementById('events-data').textContent);
    reload(eventsData, $(".event-list"));
});