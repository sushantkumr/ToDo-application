window.s = self;
function getTaskId() {
	taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )
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
	taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )
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
	const taskId = window.location.pathname.substr(window.location.pathname.lastIndexOf('/') +1 )
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


$(document).ready(function() {
    getTaskId();
});
