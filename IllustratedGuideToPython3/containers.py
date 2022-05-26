names = list()
names.append("Justice")
names.append("Larry")
# list = []
# tuples = ()
# sets = {}


names.append("Jake")
names.sort()
print(names)

info_jay = ('Justice', 'Bole', '26')
people = list()
people.append(info_jay)
print(people)
info_mary = ('Bary', 'Keim', "26")
people.append(info_mary)
print(people)
people.sort()
print(people)

friends_names = {"James", "Justice", "Jake", "Allie", "Breanna", "Diana", "Stacie", "George", "Piper"}
top_names = {'James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth'}

same_names = friends_names & top_names
print(same_names)

shakespeare_page = '''SCENE III. Room in Capulet’s House.
Enter Lady Capulet and Nurse.
LADY CAPULET.
Nurse, where’s my daughter? Call her forth to me.
NURSE.
Now, by my maidenhead, at twelve year old,
I bade her come. What, lamb! What ladybird!
God forbid! Where’s this girl? What, Juliet!
Enter Juliet.
JULIET.
How now, who calls?
NURSE.
Your mother.
JULIET.
Madam, I am here. What is your will?
LADY CAPULET.
This is the matter. Nurse, give leave awhile,
We must talk in secret. Nurse, come back again,
I have remember’d me, thou’s hear our counsel.
Thou knowest my daughter’s of a pretty age.
NURSE.
Faith, I can tell her age unto an hour.
LADY CAPULET.
She’s not fourteen.
NURSE.
I’ll lay fourteen of my teeth,
And yet, to my teen be it spoken, I have but four,
She is not fourteen. How long is it now
To Lammas-tide?
LADY CAPULET.
A fortnight and odd days.
NURSE.
Even or odd, of all days in the year,
Come Lammas Eve at night shall she be fourteen.
Susan and she,—God rest all Christian souls!—
Were of an age. Well, Susan is with God;
She was too good for me. But as I said,
On Lammas Eve at night shall she be fourteen;
That shall she, marry; I remember it well.
’Tis since the earthquake now eleven years;
And she was wean’d,—I never shall forget it—,
Of all the days of the year, upon that day:
For I had then laid wormwood to my dug,
Sitting in the sun under the dovehouse wall;
My lord and you were then at Mantua:
Nay, I do bear a brain. But as I said,
When it did taste the wormwood on the nipple
Of my dug and felt it bitter, pretty fool,
To see it tetchy, and fall out with the dug!
Shake, quoth the dovehouse: ’twas no need, I trow,
To bid me trudge.
And since that time it is eleven years;
For then she could stand alone; nay, by th’rood
She could have run and waddled all about;
For even the day before she broke her brow,
And then my husband,—God be with his soul!
A was a merry man,—took up the child:
‘Yea,’ quoth he, ‘dost thou fall upon thy face?
Thou wilt fall backward when thou hast more wit;
Wilt thou not, Jule?’ and, by my holidame,
The pretty wretch left crying, and said ‘Ay’.
To see now how a jest shall come about.
I warrant, and I should live a thousand years,
I never should forget it. ‘Wilt thou not, Jule?’ quoth he;
And, pretty fool, it stinted, and said ‘Ay.’
LADY CAPULET.
Enough of this; I pray thee hold thy peace.
NURSE.
Yes, madam, yet I cannot choose but laugh,
To think it should leave crying, and say ‘Ay’;
And yet I warrant it had upon it brow
A bump as big as a young cockerel’s stone;
A perilous knock, and it cried bitterly.
‘Yea,’ quoth my husband, ‘fall’st upon thy face?
Thou wilt fall backward when thou comest to age;
Wilt thou not, Jule?’ it stinted, and said ‘Ay’.
JULIET.
And stint thou too, I pray thee, Nurse, say I.
NURSE.
Peace, I have done. God mark thee to his grace
Thou wast the prettiest babe that e’er I nurs’d:
And I might live to see thee married once, I have my wish.
LADY CAPULET.
Marry, that marry is the very theme
I came to talk of. Tell me, daughter Juliet,
How stands your disposition to be married?
JULIET.
It is an honour that I dream not of.
NURSE.
An honour! Were not I thine only nurse,
I would say thou hadst suck’d wisdom from thy teat.
LADY CAPULET.
Well, think of marriage now: younger than you,
Here in Verona, ladies of esteem,
Are made already mothers. By my count
I was your mother much upon these years
That you are now a maid. Thus, then, in brief;
The valiant Paris seeks you for his love.
NURSE.
A man, young lady! Lady, such a man
As all the world—why he’s a man of wax.
LADY CAPULET.
Verona’s summer hath not such a flower.
NURSE.
Nay, he’s a flower, in faith a very flower.
LADY CAPULET.
What say you, can you love the gentleman?
This night you shall behold him at our feast;
Read o’er the volume of young Paris’ face,
And find delight writ there with beauty’s pen.
Examine every married lineament,
And see how one another lends content;
And what obscur’d in this fair volume lies,
Find written in the margent of his eyes.
This precious book of love, this unbound lover,
To beautify him, only lacks a cover:
The fish lives in the sea; and ’tis much pride
For fair without the fair within to hide.
That book in many’s eyes doth share the glory,
That in gold clasps locks in the golden story;
So shall you share all that he doth possess,
By having him, making yourself no less.
NURSE.
No less, nay bigger. Women grow by men.
LADY CAPULET.
Speak briefly, can you like of Paris’ love?
JULIET.
I’ll look to like, if looking liking move:
But no more deep will I endart mine eye
Than your consent gives strength to make it fly.
Enter a Servant.
SERVANT.
Madam, the guests are come, supper served up, you called, my young lady asked for, the Nurse cursed in the pantry, and everything in extremity. I must hence to wait, I beseech you follow straight.
LADY CAPULET.
We follow thee.
[Exit Servant.]
Juliet, the County stays.
NURSE.
Go, girl, seek happy nights to happy days.
[Exeunt.]'''
shakespeare_split = shakespeare_page.split()

ralph_page = '''I
POEMS
* * * * *
GOOD-BYE
Good-bye, proud world! I'm going home:
Thou art not my friend, and I'm not thine.
Long through thy weary crowds I roam;
A river-ark on the ocean brine,
Long I've been tossed like the driven foam:
But now, proud world! I'm going home.
Good-bye to Flattery's fawning face;
To Grandeur with his wise grimace;
To upstart Wealth's averted eye;
To supple Office, low and high;
To crowded halls, to court and street;
To frozen hearts and hasting feet;
To those who go, and those who come;
Good-bye, proud world! I'm going home.
I am going to my own hearth-stone,
Bosomed in yon green hills alone,—
secret nook in a pleasant land,
Whose groves the frolic fairies planned;
Where arches green, the livelong day,
Echo the blackbird's roundelay,
And vulgar feet have never trod
A spot that is sacred to thought and God.
O, when I am safe in my sylvan home,
I tread on the pride of Greece and Rome;
And when I am stretched beneath the pines,
Where the evening star so holy shines,
I laugh at the lore and the pride of man,
At the sophist schools and the learned clan;
For what are they all, in their high conceit,
When man in the bush with God may meet?
EACH AND ALL
Little thinks, in the field, yon red-cloaked clown
Of thee from the hill-top looking down;
The heifer that lows in the upland farm,
Far-heard, lows not thine ear to charm;
The sexton, tolling his bell at noon,
Deems not that great Napoleon
Stops his horse, and lists with delight,
Whilst his files sweep round yon Alpine height;
Nor knowest thou what argument
Thy life to thy neighbor's creed has lent.
All are needed by each one;
Nothing is fair or good alone.
I thought the sparrow's note from heaven,
Singing at dawn on the alder bough;
I brought him home, in his nest, at even;
He sings the song, but it cheers not now,
For I did not bring home the river and sky;—
He sang to my ear,—they sang to my eye.
The delicate shells lay on the shore;
The bubbles of the latest wave
Fresh pearls to their enamel gave,
And the bellowing of the savage sea
Greeted their safe escape to me.
I wiped away the weeds and foam,
I fetched my sea-born treasures home;
But the poor, unsightly, noisome things
Had left their beauty on the shore
With the sun and the sand and the wild uproar.
The lover watched his graceful maid,
As 'mid the virgin train she strayed,
Nor knew her beauty's best attire
Was woven still by the snow-white choir.
At last she came to his hermitage,
Like the bird from the woodlands to the cage;—
The gay enchantment was undone,
A gentle wife, but fairy none.
Then I said, 'I covet truth;
Beauty is unripe childhood's cheat;
I leave it behind with the games of youth:'—
As I spoke, beneath my feet
The ground-pine curled its pretty wreath,
Running over the club-moss burrs;
I inhaled the violet's breath;
Around me stood the oaks and firs;
Pine-cones and acorns lay on the ground;
Over me soared the eternal sky.
Full of light and of deity;
Again I saw, again I heard,
The rolling river, the morning bird;—
Beauty through my senses stole;
I yielded myself to the perfect whole.
THE PROBLEM
I like a church; I like a cowl;
I love a prophet of the soul;
And on my heart monastic aisles
Fall like sweet strains, or pensive smiles
Yet not for all his faith can see
Would I that cowlèd churchman be.
Why should the vest on him allure,
Which I could not on me endure?
Not from a vain or shallow thought
His awful Jove young Phidias brought;
Never from lips of cunning fell
The thrilling Delphic oracle;
Out from the heart of nature rolled
The burdens of the Bible old;
The litanies of nations came,
Like the volcano's tongue of flame,
Up from the burning core below,—
The canticles of love and woe:
The hand that rounded Peter's dome
And groined the aisles of Christian Rome
Wrought in a sad sincerity;
Himself from God he could not free;
He builded better than he knew;—
The conscious stone to beauty grew.
Know'st thou what wove yon woodbird's nest
Of leaves, and feathers from her breast?
Or how the fish outbuilt her shell,
Painting with morn each annual cell?
Or how the sacred pine-tree adds
To her old leaves new myriads?
Such and so grew these holy piles,
Whilst love and terror laid the tiles.
Earth proudly wears the Parthenon,
As the best gem upon her zone,
And Morning opes with haste her lids
To gaze upon the Pyramids;
O'er England's abbeys bends the sky,
As on its friends, with kindred eye;
For out of Thought's interior sphere
These wonders rose to upper air;
And Nature gladly gave them place,
Adopted them into her race,
And granted them an equal date
With Andes and with Ararat.
These temples grew as grows the grass;
Art might obey, but not surpass.
The passive Master lent his hand
To the vast soul that o'er him planned;
And the same power that reared the shrine
Bestrode the tribes that knelt within.
Ever the fiery Pentecost
Girds with one flame the countless host,
Trances the heart through chanting choirs,
And through the priest the mind inspires.
The word unto the prophet spoken
Was writ on tables yet unbroken;
The word by seers or sibyls told,
In groves of oak, or fanes of gold,
Still floats upon the morning wind,
Still whispers to the willing mind.
One accent of the Holy Ghost
The heedless world hath never lost.
I know what say the fathers wise,—
The Book itself before me lies,
Old Chrysostom, best Augustine,
And he who blent both in his line,
The younger Golden Lips or mines,
Taylor, the Shakspeare of divines.
His words are music in my ear,
I see his cowlèd portrait dear;
And yet, for all his faith could see,
I would not the good bishop be.'''

shakespeare_split = shakespeare_page.split()
ralph_split = ralph_page.split()

shakespeare_set = set(shakespeare_split)
ralph_set = set(ralph_split)


common_words = shakespeare_set & ralph_set
print(common_words)

unique_words = shakespeare_set ^ ralph_set
print(unique_words)

list_set = set(dir(list))
tuple_set = set(dir(tuple))

list_exclusives = list_set - tuple_set
print(list_exclusives)