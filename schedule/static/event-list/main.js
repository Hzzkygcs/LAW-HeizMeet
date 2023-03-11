function reload(eventsData, parentEl){
    console.log("reload")
    parentEl = $(parentEl);
    const eventItemTemplate = $("#event-item-template");

    for (const event of eventsData) {
        const newEl = $(eventItemTemplate.html());
        const {name, id} = event;
        newEl.find(".event-name").text(name);
        parentEl.append(newEl);

        const delBtn = newEl.find(".delete-btn");
        delBtn.click(((name, id) => (e) => {
            deleteEvent(id);
        })(name, id));

    }
}

function deleteEvent(eventId){
    $.ajax({
        url: '/events/' + eventId,
        type: 'DELETE',
        success: function(result) {
            console.assert(result.success === 1);
            location.reload();
        }
    });
}


$(document).ready((e) => {
    let eventsData = JSON.parse(document.getElementById('events-data').textContent);
    reload(eventsData, $(".event-list"));
});