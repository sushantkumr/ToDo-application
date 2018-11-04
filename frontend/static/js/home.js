function getTasks() {

    titleSearch = document.getElementById('searchByTitle').value;
    periodSearch = document.getElementById('searchByPeriod').value;
    taskNode = document.getElementById('tasks');
    taskNode.innerHTML = '';

    data = {}

    if (titleSearch != '') {
        data['title__contains'] = titleSearch
    }

    if (periodSearch != '') {
        data['period'] = periodSearch
    }

    url = 'api/v1/task/';
    $.ajax({
        method: 'GET',
        contentType: 'application/json',
        url: url,
        data: data,
        success: function (response) {
            document.getElementById("totalTasks").innerHTML = "Number of tasks: " + (response.meta["total_count"])
            if (response.objects) {
                $.each(response.objects, function (i, item) {
                    let aTag = document.createElement('a');
                    console.log(item);
                    aTag.classList.add('ui', 'card');
                    /*aTag.target = "_blank";*/
                    aTag.href = "/task_details/" + item.id;

                    let firstDivContent = document.createElement('div');
                    firstDivContent.classList.add('content');

                    let headerDiv = document.createElement('div');
                    headerDiv.classList.add('header');
                    headerDiv.innerHTML = item.title;

                    let statusDiv = document.createElement('div');
                    statusDiv.classList.add('meta');
                    let statusSpan = document.createElement('span');
                    statusSpan.classList.add('left', 'floated');
                    let statusSmall = document.createElement('small');
                    statusSmall.innerHTML = "Status: " + ( !item.completed ? "Pending" : "Completed" );
                    statusSpan.appendChild(statusSmall);
                    statusDiv.appendChild(statusSpan);

                    let descriptionDiv = document.createElement('div');
                    descriptionDiv.classList.add('description');
                    let descriptionPTag = document.createElement('p');
                    descriptionPTag.innerHTML = item.description;
                    descriptionDiv.appendChild(descriptionPTag);

                    let secondDivContent = document.createElement('div');
                    secondDivContent.classList.add('content');
                    let dueDateSpan = document.createElement('span');
                    dueDateSpan.classList.add('left', 'floated');
                    dueDateSpan.innerHTML = "Due: " + item.due_date;
                    secondDivContent.appendChild(dueDateSpan);

                    firstDivContent.appendChild(headerDiv);
                    firstDivContent.appendChild(statusDiv);
                    firstDivContent.appendChild(descriptionDiv);
                    aTag.appendChild(firstDivContent);
                    aTag.appendChild(secondDivContent);

                    $('#tasks').append(aTag);
                });
            }
            else {
                console.log('Error: ' + response);
            }
        },
        error: function(a, b, c) {
            console.log(a, b, c);
        }
    });
};

$(document).ready(function() {
    getTasks();
});
