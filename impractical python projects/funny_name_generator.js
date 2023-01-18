// Funny Name Generator.
// 2023-18-January
// project no 1. 2023
// code rewritten in js by : Lawi365

// SudoCode.
`Load a list of first names
Load a list of surnames
Choose a first name at random
Assign the name to a variable
Choose surname at randm 
Assing the name to another variable.
Print the names to the screen in order and in red font
Ask the user to quit or play again
If user plays again:
    repeat
If user quits:
    end and exit`

const first_names = ['Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ", 'Chad', 'Chesterfield',
    'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
    'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
    'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
    'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
    'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
    'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
    'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
    "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
    'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
    'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
    "Winston 'Jazz Hands'", 'Worms',
    'Butterbean', 'Buttermilk', 'Buttocks'];

const last_names = ['Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks'];

function choose_random_firstname(first,last){
    let choice = Math.floor(Math.random() * 10)
    let choice1 = Math.floor(Math.random() * 10)

    
    return first[choice] +' The ' + last[choice1];
};

let loop_count = 5;

for (let k=5; k<=0 ; k--)
    setTimeout(()=>{
    },3)
    console.log(choose_random_firstname(first_names,last_names));
        loop_count -= 1;
