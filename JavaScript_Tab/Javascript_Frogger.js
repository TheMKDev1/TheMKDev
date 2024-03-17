
//board
const board = document.getElementById("board");
const brush = board.getContext('2d');

let blockSize = 25;
let rows = 32;
let cols = 32;


//caric
const tick = 10;
let upInterval;
let carInterval;

let jumpTimeout;

let chanceForEmpty = 2;


//frog
let frog = {    

    x: 0,
    y: 0,

    width: blockSize,
    height: blockSize,

    veloX: 0,
    veloY: 0,

    canJump: true,

    jumpCooldown: 135,
}


//car
let cars = [];
let carIntervals = []

let minSpeed = 48;
let maxSpeed = 64;

let emptyLanes = [];


function generateCars()
{
    cars = [];
    emptyLanes = [];

    for (let r = 3; r < rows - 3; r++)
    {
        if ((Math.floor(Math.random() * (chanceForEmpty + 1) + 0) == chanceForEmpty))
        {  
            emptyLanes.push(r);
        }
        else
        {
            let car = {

                x:  (Math.floor(Math.random() * cols) + 0) * blockSize,
                y: blockSize * r,
            
                width: 2 * blockSize,
                height: blockSize,


                speed: Math.floor(Math.random() * maxSpeed) + minSpeed,
            }
    
            cars.push(car);
    
            carIntervals.push(setInterval(carMove, car.speed, cars.length - 1));
        }
    }
}


window.onload = function()
{
    document.addEventListener("keydown", jumpInput);
    reLoad();
}

function reLoad()
{
    for (let i = 0; i < carIntervals.length; i++)
    {
        clearInterval(carIntervals[i])
    }

    carIntervals = []

    board.height = rows * blockSize;
    board.width = cols * blockSize;

    generateCars();

    frog.x = (cols * 0.5) * blockSize;
    frog.y = blockSize;

    upInterval = setInterval(update, tick); 
}

function update()
{       
    brush.fillStyle = "	#989898";
    brush.fillRect(0, 0, board.width, board.height);

    for (let i = 0; i < emptyLanes.length; i++)
    {
        brush.fillStyle = "silver";
        brush.fillRect(0, emptyLanes[i] * blockSize, cols * blockSize, blockSize);
    }

    brush.fillStyle = "silver";
    brush.fillRect(0, 0, cols * blockSize, blockSize * 3);

    brush.fillRect(0, (rows - 3) * blockSize, cols * blockSize, blockSize * 3);


    brush.strokeStyle="black";

    for (let r = 0; r < cars.length; r++)
    {
        if (r % 2 == 0)
        {
            brush.fillStyle= "darkRed";
        }
        else
        {
            brush.fillStyle= "navy";
        }


        brush.fillRect(cars[r].x, cars[r].y, cars[r].width, cars[r].height);
    }

    brush.fillStyle = "limeGreen";
    brush.fillRect(frog.x, frog.y, blockSize, blockSize);

    brush.strokeStyle="black";
    brush.strokeRect(frog.x, frog.y, blockSize, blockSize);

    // car collision
    for (let i = 0; i < cars.length; i++)
    {
        if ((frog.x == cars[i].x || frog.x == cars[i].x + blockSize) && frog.y == cars[i].y)
        {
            frog.x = (cols * 0.5) * blockSize;
            frog.y = blockSize;
        }
    }

    if (frog.y == (rows - 3) * blockSize)
    {
        reLoad();
    }
}

function carMove(r)
{
    if (cars[r].x > cols * blockSize)
    {
        cars[r].x = -5 * blockSize;
    }
    else
    {
        cars[r].x = cars[r].x + blockSize;
    }
}

function jumpInput(e)
{
    if (e.code == "KeyW")
    {
        Jump(1);
    }
    else if (e.code == "KeyS")
    {
        Jump(2);
    }
    else if (e.code == "KeyD")
    {
        Jump(3);
    }
    else if (e.code == "KeyA")
    {
        Jump(4);
    }
}

function Jump(direction)
{
    if (frog.canJump)
    {
        if (direction == 1)
        {
            frog.veloY = -1;
            frog.y += frog.veloY * blockSize;

            frog.canJump = false;
            jumpTimeout = setTimeout(reJump, frog.jumpCooldown);
        }
        else if (direction == 2)
        {
            frog.veloY = 1;
            frog.y += frog.veloY * blockSize;    

            frog.canJump = false;
            jumpTimeout = setTimeout(reJump, frog.jumpCooldown);
        }
        else if (direction == 3)
        {
            frog.veloX = 1;
            frog.x += frog.veloX * blockSize;
                        
            frog.canJump = false;
            jumpTimeout = setTimeout(reJump, frog.jumpCooldown);
        }
        else if (direction == 4)
        {
            frog.veloX = -1;
            frog.x += frog.veloX * blockSize;
                        
            frog.canJump = false;
            jumpTimeout = setTimeout(reJump, frog.jumpCooldown);
        }
    }
}

function reJump()
{
    frog.canJump = true;
}