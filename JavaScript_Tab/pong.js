
// paddles

let paddle1X;
let paddle1Y;

let paddle2X;
let paddle2Y;

let paddleWidth = 15;
let paddleHeight = 200;

let moveSpeed = 100;


// ball

let ballSpeed = 4;
let ballSize = 16;

let ballX;
let ballY;

let ballYVelo;
let ballXVelo;

let ballSpeedMultiplier = 0.1;
let ballMaxSpeed = 12;

let ballAddedSpeed = 0;


// game logic

let hitCount;
let countedHit;

let p1Score;
let p2Score; 

let isRed;

let P1RobotActive = true;
let P1RobotPos = 3;
let P1RobotAccuracy = 40;

let P2RobotActive = true;
let P2RobotPos = 3;
let P2RobotAccuracy = 40;


// board

let board;
let brush;

let lines = 10;
let distBTWLines = 95;

let linesWidth = 6;
let linesHeight = 35;


let tick = 10;

let upInterval;


window.onload = function()
{
    board = document.getElementById("board");
    brush = board.getContext('2d');

    document.addEventListener("keydown", move);

    reLoad();

    p1Score = 0;
    p2Score = 0;
    hitCount = 0;
}


function reLoad()
{
    clearInterval(upInterval);

    // reset the paddles
    paddle1Y = (board.height * 0.5) - (paddleHeight * 0.5);
    paddle2Y = (board.height * 0.5) - (paddleHeight * 0.5);

    paddle1X = 25;
    paddle2X = (board.width - paddle1X) - paddleWidth;

    // reset the ball
    ballXVelo = Math.round(Math.random()) * 2 - 1;
    ballYVelo = Math.round(Math.random()) * 2 -1;

    ballX = board.width * 0.5;
    ballY = Math.floor(Math.random() * (board.height - 100)) + 50;

    hitCount = 0;
    countedHit = false;
    
    upInterval = setInterval(update, tick);
}


function update()
{

    brush.fillStyle="darkgray";
    brush.fillRect(0,0, board.width, board.height);

    for (let i = 0.8; i <= lines; i++)
    {
        brush.fillStyle="gray";
        brush.fillRect(board.width * 0.5, distBTWLines * i, linesWidth, linesHeight);
    }

    brush.fillStyle="dimGray";
    brush.font="50px Tahoma";

    if (hitCount <= 9)
    {
        brush.fillText("0" + hitCount, (board.width * 0.5) - 25, 50);
    }
    else
    {
        brush.fillText(hitCount, (board.width * 0.5) - 20, 50);
    }

    
    brush.font="100px Tahoma";

    brush.fillStyle="darkRed";
    brush.fillText(p1Score, (board.width * 0.5) -150, 125);

    brush.fillStyle="darkBlue";
    brush.fillText(p2Score, (board.width * 0.5) + 100, 125);


    // ball
    if (ballX <= board.width * 0.5)
    {
        brush.fillStyle="maroon";

        isRed = true;
    }
    else
    {
        brush.fillStyle="midNightBlue";
    }

    brush.strokeStyle = 'black';
    brush.lineWidth = 5;
    
    brush.beginPath();
    
    brush.arc(ballX, ballY, ballSize, 0, 2*Math.PI, false);
    
    brush.stroke();
    brush.fill();


    // paddle 1
    brush.fillStyle="crimson";
    brush.fillRect(paddle1X, paddle1Y, paddleWidth, paddleHeight);

    brush.strokeStyle="black";
    brush.strokeRect(paddle1X, paddle1Y, paddleWidth, paddleHeight)

    // paddle 2
    brush.fillStyle="mediumBlue";
    brush.fillRect((board.width - paddle1X) - paddleWidth, paddle2Y, paddleWidth, paddleHeight);

    brush.strokeStyle="black";
    brush.strokeRect(paddle2X, paddle2Y, paddleWidth, paddleHeight)

    
    //P1 robot algorithim

    if (P1RobotActive == true)
    {

        if (ballX < board.width * 0.5)
        {
            P1RobotAccuracy = 40;
        }
        else
        {
            P1RobotAccuracy = -240;
        }

        if ((ballY > (paddle1Y + P1RobotAccuracy)) && (P1RobotPos <= 6))
        {
            P1RobotPos += 1;    
        }
        if ((ballY < (paddle1Y + paddleHeight - P1RobotAccuracy)) && (P1RobotPos >= 0))
        {
            P1RobotPos -= 1;
        }

        if ((P1RobotPos >= 0) && (P1RobotPos <= 6))
        {
            paddle1Y = P1RobotPos * 100
        }

    }


    //P2 robot algorithim
    if (P2RobotActive == true)
    {

        if (ballX > board.width * 0.5)
        {
            P2RobotAccuracy = 40;
        }
        else
        {
            P2RobotAccuracy = -240;
        }

        if ((ballY > (paddle2Y + P2RobotAccuracy)) && (P2RobotPos <= 6))
        {
            P2RobotPos += 1;    
        }
        if ((ballY < (paddle2Y + paddleHeight - P2RobotAccuracy)) && (P2RobotPos >= 0))
        {
            P2RobotPos -= 1;
        }

        if ((P2RobotPos >= 0) && (P2RobotPos <= 6))
        {
            paddle2Y = P2RobotPos * 100
        }

    }   


    // ball collision
    
    // board collision
    if (ballY >= board.height - ballSize)
    {
        ballYVelo = ballYVelo * -1;
    }
    else if (ballY <= ballSize)
    {
        ballYVelo = ballYVelo * -1;
    }

    if (ballX <= ballSize)
    {
        p2Score++;

        P1RobotActive = true;

        reLoad();
    }
    else if (ballX >= board.width - ballSize)
    {
        p1Score++;

        P2RobotActive = true;

        reLoad();
    }


    // paddle collision
    if(ballX - ballSize <= paddle1X + paddleWidth && ballY >= paddle1Y && ballY <= (paddle1Y + paddleHeight))
    {
        ballXVelo = 1;

        countHit();
    }

    if(ballX + ballSize >= paddle2X && ballY >= paddle2Y && ballY <= (paddle2Y + paddleHeight))
    {
        ballXVelo = -1;

        countHit();
    }


    // ball movement
    if ((ballSpeed + ballAddedSpeed) <= ballMaxSpeed)
    {
        ballAddedSpeed = hitCount * ballSpeedMultiplier;
    }

    console.log(ballAddedSpeed);

    ballX = ballX + ((ballSpeed + ballAddedSpeed) * ballXVelo);
    ballY = ballY + ((ballSpeed+ ballAddedSpeed) * ballYVelo);
}


function move(e)
{
    if (e.code == "KeyW" && paddle1Y != 0)
    {
        if (P1RobotActive == true)
        {
            P1RobotActive = false;
        }

        paddle1Y -= moveSpeed;
    }
    else if (e.code == "KeyS" && paddle1Y != board.height - paddleHeight)
    {
        if (P1RobotActive == true)
        {
            P1RobotActive = false;
        }

        paddle1Y += moveSpeed;
    }


    if (e.code == "KeyI" && paddle2Y != 0)
    {
        if (P2RobotActive == true)
        {
            P2RobotActive = false;
        }

        paddle2Y -= moveSpeed;
    }
    else if (e.code == "KeyK" && paddle2Y != board.height - paddleHeight)
    {
        if (P2RobotActive == true)
        {
            P2RobotActive = false;
        }

        paddle2Y += moveSpeed;
    }
}


function countHit()
{
    if (countedHit)
    {

    }
    else
    {
        hitCount++;
        countedHit = true;
        setTimeout(setCountedHit, 500)
    }

}


function setCountedHit()
{
    countedHit = false;
}

// banana power

