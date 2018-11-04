function onSubmit(event) {
	event.preventDefault();
	host = 'http://' + window.location.host
    url = host + '/api/v1/task/';
    taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )

	data = {
		'title': document.getElementById("newTask").elements["title"].value,
		'description': document.getElementById("newTask").elements["description"].value,
		'due_date': document.getElementById("newTask").elements["dueDate"].value,
		'alert_time': document.getElementById("newTask").elements["alertTime"].value,
	}

    if (taskId) {
        data['parent_task_id'] = taskId
    }

    $.ajax({
        method: 'POST',
        contentType: 'application/json',
        url: url,
        data: JSON.stringify(data),
        success: (data, textStatus, xhr) => {
            if (xhr.status == 201) {
    			window.location = "/";
            }
            else {
                console.log('Error: ' + data);
            }
        },
        error: function(a, b, c) {
            console.log(a, b, c);
        }
    });	
}