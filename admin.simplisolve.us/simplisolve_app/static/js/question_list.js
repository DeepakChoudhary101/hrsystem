// interview.js

document.addEventListener('DOMContentLoaded', function () {
    const addTopicButton = document.getElementById('add-topic');
    const topicList = document.getElementById('topic-list');
    const addQuestionButton = document.getElementById('add-question');
    const questionList = document.getElementById('question-list');

    // Add topic button click event
    addTopicButton.addEventListener('click', function () {
        const topicInput = document.getElementById('topics');
        const selectedTopic = topicInput.options[topicInput.selectedIndex].text;
        const topicItem = document.createElement('li');
        topicItem.textContent = selectedTopic;
        topicList.appendChild(topicItem);
    });

    // Add question button click event
    addQuestionButton.addEventListener('click', function () {
        const questionInput = document.getElementById('question').value;
        const marksInput = document.getElementById('marks').value;
        const questionItem = document.createElement('li');
        questionItem.textContent = `Question: ${questionInput}, Marks: ${marksInput}`;
        questionList.appendChild(questionItem);
    });
});
