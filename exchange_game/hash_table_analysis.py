from hash_table import LinearProbePotionTable
import random


def analysis(item_size, good_hash=True):
    """
    Approach Taken :
    We have parameters item size to change the number of items from list taken and good_hash which is boolean to set to
    either good or bad hash. We import random and set the seed to 0 so that the random numbers are always the same. We
    create the hash table by calling LinearProbePotionTable. We have a temporary list where we append numbers till 1000
    which is the number of names in our name list. Then we use another for loop in the range of item_size parameter
    where we use the random choice method to pick a random number in the range 1000 as it will be used as the index to
    pick an item from the list. We also remove this number from the list of range 1000 so this number isn't picked again.
    Next, we hash the name by setting the key from the name list with index x and set data as the chosen name. Lastly,
    we just return the statistics method which prints the Conflict Count, Probe Total, Probe Max

    The testers at the bottom of the file change item range from 10 to 1000 and also check for the same items whats the
    difference for Good Hash and Bad Hash and print both. The text is a comma-separated paragraph so we need to use
    txt.split to make 1000 words separate strings in the list.
    """

    random.seed(0)
    hash_table = LinearProbePotionTable(item_size, good_hash)

    range_lst = []
    for i in range(len(names_list)):
        range_lst.append(i)

    for i in range(item_size):
        x = random.choice(range_lst)
        range_lst.remove(x)
        hash_table[names_list[x]] = names_list[x]

    out = (hash_table.statistics())
    return out


txt = \
    "Michael,Christopher,Jessica,Matthew,Ashley,Jennifer,Joshua,Amanda,Daniel,David,James,Robert,John,Joseph,Andrew," \
    "Ryan,Brandon,Jason,Justin,Sarah,William,Jonathan,Stephanie,Brian,Nicole,Nicholas,Anthony,Heather,Eric,Elizabeth," \
    "Adam,Megan,Melissa,Kevin,Steven,Thomas,Timothy,Christina,Kyle,Rachel,Laura,Lauren,Amber,Brittany,Danielle," \
    "Richard,Kimberly,Jeffrey,Amy,Crystal,Michelle,Tiffany,Jeremy,Benjamin,Mark,Emily,Aaron,Charles,Rebecca,Jacob," \
    "Stephen,Patrick,Sean,Erin,Zachary,Jamie,Kelly,Samantha,Nathan,Sara,Dustin,Paul,Angela,Tyler,Scott,Katherine," \
    "Andrea,Gregory,Erica,Mary,Travis,Lisa,Kenneth,Bryan,Lindsey,Kristen,Jose,Alexander,Jesse,Katie,Lindsay,Shannon," \
    "Vanessa,Courtney,Christine,Alicia,Cody,Allison,Bradley,Samuel,Shawn,April,Derek,Kathryn,Kristin,Chad,Jenna,Tara," \
    "Maria,Krystal,Jared,Anna,Edward,Julie,Peter,Holly,Marcus,Kristina,Natalie,Jordan,Victoria,Jacqueline,Corey,Keith," \
    "Monica,Juan,Donald,Cassandra,Meghan,Joel,Shane,Phillip,Patricia,Brett,Ronald,Catherine,George,Antonio,Cynthia," \
    "Stacy,Kathleen,Raymond,Carlos,Brandi,Douglas,Nathaniel,Ian,Craig,Brandy,Alex,Valerie,Veronica,Cory,Whitney,Gary," \
    "Derrick,Philip,Luis,Diana,Chelsea,Leslie,Caitlin,Leah,Natasha,Erika,Casey,Latoya,Erik,Dana,Victor,Brent,Dominique," \
    "Frank,Brittney,Evan,Gabriel,Julia,Candice,Karen,Melanie,Adrian,Stacey,Margaret,Sheena,Wesley,Vincent,Alexandra," \
    "Katrina,Bethany,Nichole,Larry,Jeffery,Curtis,Carrie,Todd,Blake,Christian,Randy,Dennis,Alison,Trevor,Seth,Kara," \
    "Joanna,Rachael,Luke,Felicia,Brooke,Austin,Candace,Jasmine,Jesus,Alan,Susan,Sandra,Tracy,Kayla,Nancy,Tina,Krystle," \
    "Russell,Jeremiah,Carl,Miguel,Tony,Alexis,Gina,Jillian,Pamela,Mitchell,Hannah,Renee,Denise,Molly,Jerry,Misty,Mario," \
    "Johnathan,Jaclyn,Brenda,Terry,Lacey,Shaun,Devin,Heidi,Troy,Lucas,Desiree,Jorge,Andre,Morgan,Drew,Sabrina,Miranda," \
    "Alyssa,Alisha,Teresa,Johnny,Meagan,Allen,Krista,Marc,Tabitha,Lance,Ricardo,Martin,Chase,Theresa,Melinda,Monique," \
    "Tanya,Linda,Kristopher,Bobby,Caleb,Ashlee,Kelli,Henry,Garrett,Mallory,Jill,Jonathon,Kristy,Anne,Francisco,Danny," \
    "Robin,Lee,Tamara,Manuel,Meredith,Colleen,Lawrence,Christy,Ricky,Randall,Marissa,Ross,Mathew,Jimmy,Abigail,Kendra," \
    "Carolyn,Billy,Deanna,Jenny,Jon,Albert,Taylor,Lori,Rebekah,Cameron,Ebony,Wendy,Angel,Micheal,Kristi,Caroline,Colin," \
    "Dawn,Kari,Clayton,Arthur,Roger,Roberto,Priscilla,Darren,Kelsey,Clinton,Walter,Louis,Barbara,Isaac,Cassie,Grant," \
    "Cristina,Tonya,Rodney,Bridget,Joe,Cindy,Oscar,Willie,Maurice,Jaime,Angelica,Sharon,Julian,Jack,Jay,Calvin,Marie," \
    "Hector,Kate,Adrienne,Tasha,Michele,Ana,Stefanie,Cara,Alejandro,Ruben,Gerald,Audrey,Kristine,Ann,Shana,Javier," \
    "Katelyn,Brianna,Bruce,Deborah,Claudia,Carla,Wayne,Roy,Virginia,Haley,Brendan,Janelle,Jacquelyn,Beth,Edwin,Dylan," \
    "Dominic,Latasha,Darrell,Geoffrey,Savannah,Reginald,Carly,Fernando,Ashleigh,Aimee,Regina,Mandy,Sergio,Rafael,Pedro," \
    "Janet,Kaitlin,Frederick,Cheryl,Autumn,Tyrone,Martha,Omar,Lydia,Jerome,Theodore,Abby,Neil,Shawna,Sierra,Nina," \
    "Tammy,Nikki,Terrance,Donna,Claire,Cole,Trisha,Bonnie,Diane,Summer,Carmen,Mayra,Jermaine,Eddie,Micah,Marvin,Levi," \
    "Emmanuel,Brad,Taryn,Toni,Jessie,Evelyn,Darryl,Ronnie,Joy,Adriana,Ruth,Mindy,Spencer,Noah,Raul,Suzanne,Sophia,Dale," \
    "Jodi,Christie,Raquel,Naomi,Kellie,Ernest,Jake,Grace,Tristan,Shanna,Hilary,Eduardo,Ivan,Hillary,Yolanda,Alberto," \
    "Andres,Olivia,Armando,Paula,Amelia,Sheila,Rosa,Robyn,Kurt,Dane,Glenn,Nicolas,Gloria,Eugene,Logan,Steve,Ramon,Bryce," \
    "Tommy,Preston,Keri,Devon,Alana,Marisa,Melody,Rose,Barry,Marco,Karl,Daisy,Leonard,Randi,Maggie,Charlotte,Emma," \
    "Terrence,Justine,Britney,Lacy,Jeanette,Francis,Tyson,Elise,Sylvia,Rachelle,Stanley,Debra,Brady,Charity,Hope,Melvin," \
    "Johanna,Karla,Jarrod,Charlene,Gabrielle,Cesar,Clifford,Byron,Terrell,Sonia,Julio,Stacie,Shelby,Shelly,Edgar,Roxanne," \
    "Dwayne,Kaitlyn,Kasey,Jocelyn,Alexandria,Harold,Esther,Kerri,Ellen,Abraham,Cedric,Carol,Katharine,Shauna,Frances," \
    "Antoine,Tabatha,Annie,Erick,Alissa,Sherry,Chelsey,Franklin,Branden,Helen,Traci,Lorenzo,Dean,Sonya,Briana,Angelina," \
    "Trista,Bianca,Leticia,Tia,Kristie,Stuart,Laurie,Harry,Leigh,Elisabeth,Alfredo,Aubrey,Ray,Arturo,Joey,Kelley,Max," \
    "Andy,Latisha,Johnathon,India,Eva,Ralph,Yvonne,Warren,Kirsten,Miriam,Kelvin,Lorena,Staci,Anita,Rene,Cortney,Orlando," \
    "Carissa,Jade,Camille,Leon,Paige,Marcos,Elena,Brianne,Dorothy,Marshall,Daryl,Colby,Terri,Gabriela,Brock,Gerardo," \
    "Jane,Nelson,Tamika,Alvin,Chasity,Trent,Jana,Enrique,Tracey,Antoinette,Jami,Earl,Gilbert,Damien,Janice,Christa," \
    "Tessa,Kirk,Yvette,Elijah,Howard,Elisa,Desmond,Clarence,Alfred,Darnell,Breanna,Kerry,Nickolas,Maureen,Karina," \
    "Roderick,Rochelle,Rhonda,Keisha,Irene,Ethan,Alice,Allyson,Hayley,Trenton,Beau,Elaine,Demetrius,Cecilia,Annette," \
    "Brandie,Katy,Tricia,Bernard,Wade,Chance,Bryant,Zachery,Clifton,Julianne,Angelo,Elyse,Lyndsey,Clarissa,Meaghan," \
    "Tanisha,Ernesto,Isaiah,Xavier,Clint,Jamal,Kathy,Salvador,Jena,Marisol,Darius,Guadalupe,Chris,Patrice,Jenifer,Lynn," \
    "Landon,Brenton,Sandy,Jasmin,Ariel,Sasha,Juanita,Israel,Ericka,Quentin,Jayme,Damon,Heath,Kira,Ruby,Rita,Tiara," \
    "Jackie,Jennie,Collin,Lakeisha,Kenny,Norman,Leanne,Hollie,Destiny,Shelley,Amie,Callie,Hunter,Duane,Sally,Serena," \
    "Lesley,Connie,Dallas,Simon,Neal,Laurel,Eileen,Lewis,Bobbie,Faith,Brittani,Shayla,Eli,Judith,Terence,Ciara,Charlie," \
    "Alyson,Vernon,Alma,Quinton,Nora,Lillian,Leroy,Joyce,Chrystal,Marquita,Lamar,Ashlie,Kent,Emanuel,Joanne,Gavin," \
    "Yesenia,Perry,Marilyn,Graham,Constance,Lena,Allan,Juliana,Jayson,Shari,Nadia,Tanner,Isabel,Becky,Rudy,Blair," \
    "Christen,Rosemary,Marlon,Glen,Genevieve,Damian,Michaela,Shayna,Marquis,Fredrick,Celeste,Bret,Betty,Kurtis,Rickey," \
    "Dwight,Rory,Mia,Josiah,Norma,Bridgette,Shirley,Sherri,Noelle,Chantel,Alisa,Zachariah,Jody,Christin,Julius,Gordon," \
    "Latonya,Lara,Lucy,Jarrett,Elisha,Deandre,Audra,Beverly,Felix,Alejandra,Nolan,Tiffani,Lonnie,Don,Darlene,Rodolfo," \
    "Terra,Sheri,Iris,Maxwell,Kendall,Ashly,Kendrick,Jean,Jarvis,Fred,Tierra,Abel,Pablo,Maribel,Donovan,Stephan,Judy," \
    "Elliott,Tyrell,Chanel,Miles,Fabian,Alfonso,Cierra,Mason,Larissa,Elliot,Brenna,Bradford,Kristal,Gustavo,Gretchen," \
    "Derick,Jarred,Pierre,Lloyd,Jolene,Marlene,Leo,Jamar,Dianna,Noel,Angie,Tatiana,Rick,Leann,Corinne,Sydney,Belinda," \
    "Lora,Mackenzie,Herbert,Guillermo,Tameka,Elias,Janine,Ben,Stefan,Josephine,Dominick,Jameson,Bobbi,Blanca,Josue," \
    "Esmeralda,Darin,Ashely,Clay,Cassidy,Roland,Ismael,Harrison,Lorraine,Owen,Daniela,Rocky,Marisela,Saul,Kory,Dexter," \
    "Chandra,Gwendolyn,Francesca,Alaina,Mandi,Fallon,Celia,Vivian,Rolando,Raven,Lionel,Carolina,Tania,Joann,Casandra," \
    "Betsy,Tracie,Dante,Trey,Margarita,Skyler,Sade,Lyndsay,Jacklyn,Marina,Rogelio,Racheal,Mollie,Liliana,Maegan,Felipe," \
    "Malcolm,Santana,Anastasia,Madeline,Breanne,Tiffanie,Dillon,Melisa,Darrin,Carlton,Cornelius,Precious,Ivy,Lea," \
    "Susana,Loren,Jeff,Chiquita,Teri,Tera,Caitlyn,Hailey,Donte,Oliver,Natalia,Cherie,Lakisha,Karissa,Jeannette,Ariana," \
    "Lucia,Jerrod,Kassandra,Guy,Milton,Micaela,Krystina,Esteban,Gilberto,Chelsie,Antwan,Cathy,Ty,Shante,Roman,Kylie," \
    "Mercedes,Dena,Christi,Latrice,Kellen,Freddie,Clara,Rosanna,Demarcus,Domonique,Alvaro,Shaina,Nathanael,Kacie,Jodie," \
    "Dusty,Sidney,Adrianne,Mike,Chloe,Alecia,Sam,Rocio"
names_list = txt.split(",")

print("Columns are as shown below : ")
print("Conflict Count, Probe Total, Probe Max")
print("")
print("1. Items = 10")
print("Good Hash : " + str(analysis(10, True)))
print("Bad Hash : " + str(analysis(10, False)))
print("")
print("2. Items = 25")
print("Good Hash : " + str(analysis(25, True)))
print("Bad Hash : " + str(analysis(25, False)))
print("")
print("3. Items = 50")
print("Good Hash : " + str(analysis(50, True)))
print("Bad Hash : " + str(analysis(50, False)))
print("")
print("4. Items = 100")
print("Good Hash : " + str(analysis(100, True)))
print("Bad Hash : " + str(analysis(100, False)))
print("")
print("5. Items = 250")
print("Good Hash : " + str(analysis(250, True)))
print("Bad Hash : " + str(analysis(250, False)))
print("")
print("6. Items = 500")
print("Good Hash : " + str(analysis(500, True)))
print("Bad Hash : " + str(analysis(500, False)))
print("")
print("7. Items = 1000")
print("Good Hash : " + str(analysis(1000, True)))
print("Bad Hash : " + str(analysis(1000, False)))
