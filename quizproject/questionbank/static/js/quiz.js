function submitAnswers(answer)
    {

    var total = answers.length;
    var score = 0;
    var choice = []


    //getting choices 
    //new dynamic method 1
    for(var i = 1; i <= total; i++){
        
        choice[i] = document.forms["quizForm"]["q"+i].value;
        
    }

    //check answer
    // new dynamic method 1 for checking answer
    for(i = 1; i <= total; i++){
        if(choice[i] == answers[i - 1]){
            score++;
        }
    }

    //Display Result
    var results = document.getElementById('results');
    
    results.innerHTML = "<h3>You scored <span>" + score + "</span> out of <span>" + total + "</span></h3>"
    //alert("You scored " + score + " out of " + total);
    document.getElementById('quizsection').style.visibility = "hidden"; 
    return false;
    }