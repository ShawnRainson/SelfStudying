const tasks = ["Learn JS", "Go to shopping", "Sleep"];

function ShowTasks(taskList) {
    for(let task of taskList) {
        console.log(`Task: ${task}`);
    };
};

function AddTask(task, taskList) {
    taskList.push(task);
};

ShowTasks(tasks);
let newTask = "Sent answers to sensei"
AddTask(newTask, tasks);
ShowTasks(tasks);