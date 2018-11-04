const taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )

function getTaskDetails() {
	host = 'http://' + window.location.host
    url = host + '/api/v1/task/' + taskId;
    $.ajax({
        method: 'GET',
        contentType: 'application/json',
        url: url,
        success: (response) => {
            if (response) {
    			document.getElementById('titleData').innerHTML = response.title;
    			document.getElementById('descriptionData').innerHTML = response.description;
    			document.getElementById('dueDateData').innerHTML = (response.due_date ? response.due_date : "NOT SET");
    			document.getElementById('alertTimeData').innerHTML = (response.alert_time ? response.alert_time : "NOT SET");
    			statusNode = document.getElementById('statusData')
    			statusNode.innerHTML = (!response.completed ? "PENDING" : "COMPLETED" );
    			(!response.completed ? statusNode.classList.add('negative') : statusNode.classList.add('positive'));
            }
            else {
                console.log('Error: ' + data);
            }
        },
        error: function(a, b, c) {
            console.log(a, b, c);
            window.location = "/";
        }
    });	
}

function deleteTask() {
	/*taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )*/
	host = 'http://' + window.location.host
    url = host + '/api/v1/task/' + taskId + '/';
	data = {
    	'deleted': 'True'
    }
    $.ajax({
        method: 'PUT',
        contentType: 'application/json',
        url: url,
        data: JSON.stringify(data),
        success: (data, textStatus, xhr) => {
    		if(xhr.status == 204) {
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


function toggleTaskStatus() {
	/*const taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )*/
	const host = 'http://' + window.location.host
    const url = host + '/api/v1/task/' + taskId + '/';
    let completedStatus;
    const currentState = document.getElementById('statusData').innerHTML;
    (currentState == "PENDING" ? completedStatus = "True" : completedStatus = "False");
    data = {
    	'completed': completedStatus
    }
    $.ajax({
        method: 'PUT',
        contentType: 'application/json',
        url: url,
        data: JSON.stringify(data),
        success: (data, textStatus, xhr) => {
    		if(xhr.status == 204) {
    			window.location.reload();
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

function getSubTasks() {
    console.log("hello world")
    /*const taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )*/
    subTaskNode = document.getElementById('subTasks');
    subTaskNode.innerHTML = '';

    data = {
        'parent_task_id': taskId
    }
    host = 'http://' + window.location.host

    const url = host + '/api/v1/task/';
    console.log(url);
    $.ajax({
        method: 'GET',
        contentType: 'application/json',
        url: url,
        data: data,
        success: function (response) {
            document.getElementById("totalSubTasks").innerHTML = "Number of Sub-tasks: " + (response.meta["total_count"])
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

                    $('#subTasks').append(aTag);
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
    getTaskDetails();
    getSubTasks();
});
