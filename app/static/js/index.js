console.log("page loaded...");
date_service.min = new Date().toISOString().split("T")[0];

const questions = document.querySelectorAll(".question");

questions.forEach(function (question) {
    const btn = question.querySelector(".question-btn");

    btn.addEventListener("click", function () {
        question.classList.toggle("show-text");
    });
});