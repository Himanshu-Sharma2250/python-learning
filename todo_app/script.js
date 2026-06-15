let taskList = [];

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const task = taskInput.value;

    if (task) {
        taskList.push(task);
        taskInput.value = "";
        displayTasks();
    }
}

function displayTasks() {
    const taskListElement = document.getElementById("taskList");
    taskListElement.innerHTML = "";

    taskList.forEach((task, index) => {
        const li = document.createElement("li");
        li.textContent = task;
        li.appendChild(createDeleteButton(index));
        taskListElement.appendChild(li);
    });
}

function createDeleteButton(index) {
    const button = document.createElement("button");
    button.textContent = "Delete";

    button.onclick = function () {
        deleteTask(index);
    };

    return button;
}

function deleteTask(index) {
    taskList.splice(index, 1);
    displayTasks();
}