const computerChoice = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
let userOption 
let computerOption
let result

//first solution
const possibleChoices = document.querySelectorAll('button')

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
    userOption = e.target.id
    userChoiceDisplay.innerHTML = userOption 
    generateComputerChoice();
    getResult();
}))

function generateComputerChoice() {
    const randomNumber = Math.floor(Math.random()*3+1)

    if (randomNumber === 1){
        computerOption = 'rock'
    }
    if (randomNumber === 2){
        computerOption = 'paper'
    }
    if (randomNumber === 3){
        computerOption = 'scissors'
    }
    computerChoice.innerHTML = computerOption
}

function getResult(){
    if(computerOption===userOption){
        result = "Its a draw"
    }
    if (computerOption==='rock' && userOption==='paper'){
        result = 'You win !'
    }
    if (computerOption==='rock' && userOption==='scissors'){
        result = 'computer wins'
    }
    if (computerOption==='paper' && userOption==='scissors'){
        result = 'you win !'
    }
    if (computerOption==='paper' && userOption==='rock'){
        result = 'computer wins !'
    }
    if (computerOption==='scissors' && userOption==='rock'){
        result = 'you win !'
    }
    if (computerOption==='scissors' && userOption==='paper'){
        result = 'computer wins !'
    }
    resultDisplay.innerHTML = result
}