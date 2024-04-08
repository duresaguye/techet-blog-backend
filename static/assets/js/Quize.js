// Questions

const questions = [
    {
        question_id: '0',
        question: 'Which of the following is a browser?',
        options: [
            { option: 'Java' },
            { option: 'Google Chrome' },
            { option: 'Python' },
        ],
        correct_answer: 'Google Chrome'
    },

    {
        question_id: '1',
        question: 'What is the full form of CPU?',
        options: [
            { option: 'Control Processing Unit' },
            { option: 'Combined Processing Unit' },
            { option: 'Central Processing Unit' },
        ],
        correct_answer: 'Central Processing Unit'
    },

    {
        question_id: '2',
        question: 'CSS stands for Cascading Stylesheet',
        options: [
            { option: 'True' },
            { option: 'False' },
        ],
        correct_answer: 'True'
    },
]



const starQuizBtn = document.querySelector(".start-quiz-btn");
const quizContainer = document.querySelector(".quiz-container");
const nextBtn = document.querySelector(".next-btn");
const quizResultContainer = document.querySelector(".quiz-result-container");
const quizOverlay = document.querySelector(".quiz-overlay");
const quizCloseBtn = document.querySelector(".quiz-close-btn");
const retakeQuizBtn = document.querySelector(".retake-quiz-btn");
const optionsContainer = document.querySelector(".options-container");
const resultHeading = document.querySelector(".result-heading");
const scoreText = document.querySelector(".score-text");
const question = document.querySelector(".question");




let questionNumber = 0;
let totalQuestion = questions.length;
let userAnswer = "";
let userScore = 0;


const init = () => {
    questionNumber = 0;
    userScore = 0;
    nextBtn.innerText = "Next";
}


// Start Button

starQuizBtn.addEventListener("click", () => {
    init();
    quizContainer.classList.add("active");
    quizOverlay.classList.add("active");
    displayQuestions(questionNumber);
})


// Next Button

nextBtn.addEventListener("click", () => {
    checkAnswer();
    questionNumber++;
    if (questionNumber == totalQuestion - 1) {
        nextBtn.innerText = "Finish";
    }
    if (questionNumber < totalQuestion) {
        displayQuestions(questionNumber);
    } else {
        quizResultContainer.classList.add("active");
        showResult();
        quizContainer.classList.remove("active");
    }
})


// Close Button

quizCloseBtn.addEventListener("click", () => {
    quizResultContainer.classList.remove("active");
    quizContainer.classList.remove("active");
    quizOverlay.classList.remove("active");
})


// Retake Quiz Button

retakeQuizBtn.addEventListener("click", () => {
    init();
    quizResultContainer.classList.remove("active");
    quizContainer.classList.add("active");
    displayQuestions(questionNumber);
})


// Store Answer

const storeAnswer = (o) => {
    if (o) {
        userAnswer = o.target.nextElementSibling.innerText;
    } else {
        userAnswer = "";
    }
}


// Check Answer

const checkAnswer = () => {
    if (userAnswer == questions[questionNumber].correct_answer) {
        userScore++;
    } 
}


// Display Questions

const displayQuestions = (qNo) => {
    question.innerText = questions[qNo].question;

    optionsContainer.innerHTML = "";

    questions[qNo].options.forEach((o, oIndex)=> {
        const optionRadioButton = document.createElement("input");
        optionRadioButton.type = "radio";
        let optionId = "option" + oIndex;
        optionRadioButton.id = optionId;
        optionRadioButton.name = "option";
        optionRadioButton.addEventListener("change", storeAnswer);

        const optionLabel = document.createElement("label");
        optionLabel.htmlFor = optionId;
        optionLabel.classList.add("option");
        optionLabel.innerText = o.option;

        optionsContainer.appendChild(optionRadioButton);
        optionsContainer.appendChild(optionLabel);
    })
}

displayQuestions(questionNumber);


// Show the result

const showResult = () => {
    let percentage = (userScore/totalQuestion) * 100;

    if (percentage >= 60) {
        resultHeading.innerText = "Congratulations!";
    } else {
        resultHeading.innerText = "You can do better";
    }

    scoreText.innerText = `You have scored ${userScore} out of ${totalQuestion}.`;
}