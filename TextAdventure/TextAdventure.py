# Authors: Jake and Jay
# Copyright 2021

import sys  # Both imports needed for in game text delay
from time import sleep

class ANSI(): #Copied from internet -- Allows text to be color coded in game!
    def background(code):
        return "/33[{code}m".format(code=code)
    def style_text(code):
        return "/33[{code}m".format(code=code)
    def color_text(code):
        return "/33[{code}m".format(code=code)

def intro():

    print('''
                                                                        
                                                            `           
                                                           `$&7-        
                                                    .''`    ^#QB?       
                                                    ;vHQQMEjFNQ@Q|      
                           ,'`                         :DQQQQNQ@@Q`     
                           ,:,.                         -oN#QQ@@@QM:    
                            `^;^~                      `?qDH&QQ@@@QQ,   
                               :`.;`                 .|ahKRNQQQQ@#m:    
                               ;gNBo               _vX9HgQQQQS;.`       
                               `kg#N'           `^oKR#QQQQQW'           
                                LWg#J       `_|odNQQQ@@@QQQ:            
                                |NQQM-    :tHNg#QQ@@@@QQ@Q|             
                                ,g&#Q,   ,N##Q@@@@@QQQQ@@Z              
                   ';.         `ZM#Qg    -QQ@@@@@M#ggBQQx`              
                 :mH/,,^r:^`  'XN#Q@/     ZQQQ@@@@BNN##B'               
                ZQ@BXmz>^=vr^6Q#WB@Q`     ,QQQQQ@@QQNNQQr               
               .Q@@@QBROw6KDN#eoQBNH|`     x@QQQQQQQQ#QQ|               
     `.-        >Q@@@QdUqqHEx_--'?DQQd;-,'-oQ@QQQQQQQQQQJ               
   `;x*/ ,`      -ruKN@@QgDaumKNNNHgQQ#N#B#NgQ@@@@@@QQQQK               
   `;:::,r.          ,#@QQQQ@@QQQQQQBQQQQQQqim@@@@@@@@QQQ`              
     :;,:-           _XQQ@@@QQQQQQQQQQQQQQQQQQQ@@@@@@@@QQ:              
      '`'':         o@@@@QQQ@QQQQQQQQQQQQQQ@QQQQ@@@@@@@@Q;              
      _oNQQZ'      'ZQQQQQ@@@@@@@@@QQQQQQQQ@Q@@@@@@@@@@@Q`              
      vQQQQQN* `:xNQQQ@@@@@@@@@@@@@@@@@QQQQQQ@@@@@@@@@@N:               
       'O@QQQQQQQQQQ@@@Qv;;?/FSekOD#Q@@@@@@@Q@@@@@@@#t~                 
         /@@Q@@@@@@@Wv,               _uQ@@@@@@@@@i'                    
          ;R@@QDZ7;`                    `rw#QDESo/                      
            '`                                                          
                                                                        
                                                                       
    ''')

    intro_words = ('''
    A 
    You feel a sharp pain in your back and all throughout your legs...
    It's paintful
    Your harness snapped about 25 feet up in the air on the edge of a mountain.
    You've seemed to have lost all of your supplies and tools.
    All you have now is a cellphone with no service.
    You need to do something fast or you'll surely die on this frigid mountain.
    You pause to think for a moment and view your surroundings
    After a short period of time you notice there are three paths in front of you.

    Path #1: A narrow winding path leads up towards the summit of the mountain. Maybe I can get a signal if I climb higher?
    Path #2: The way back is trecherous but continuing forward seems just as dangerous. Maybe I should head back down the mountain and seek aid.
    Path #3: It's too dangerous to continue on in my condition, perhaps I can find shelter nearby.
    ''')
    for char in intro_words: #used for "typewriter" effect
      sleep(.01)  #the integer determines the speed of the text. Higher is slower.
      sys.stdout.write(char)
      sys.stdout.flush()

    firstPath = input("\nWhich way?(1/2/3): ")
    if firstPath == '1':
        path1()
    elif firstPath == '2':
        print("You decide to climb down the mountain.")
        path2()
    elif firstPath == '3':
        print("You decide to search nearby for shelter.")
        path3()

def path1():

    print('''
    QQQQQQQQQ#QQQQWR&DRDRRRN&QQQQ@@@@QQQQ@@@@@@Q@Q@@@@
    @@QQQQQQQQ@QQQB#NNNW'   DBQQQQQQQQQQQQQQ@@@@@Q@@@@
    KDBQQQ##QQQQQQQNBN&R`  `KQQQQQQQQQQQQQQBQ@@@QQ@@@@
    QQQQQQNNNNQQNQQNN#&OdHdR#QQQQQQQQQQQQQQQQQQQQQ@Q@@
    QB#RWNRN&NQB#NNN#N&d9qK9DBNDWNBBDNW#ODW#Q#QQQQQBQQ
    kKdd&BNNNDHUeePSRHSJJ/7vJS&XUOR#R9NNqUdQBBNNQBQB&O
    yuJJuoev]uzoJz]/Dz//vzJtc/9tJoe&ZeSNkoqQBqN&9HBQkX
    :;?~^F::;;::=:r^D=/|/ciz]oPKvccKzczFOSDN&keSz/U&:,
       ;,y',r;;:|?;^N||/cizzzJzuXuvPevv79eQPu?v>^:zH,`
      ::F  ~^'`;;',D::;;;^^^;;;:=cyX:~'t@tr:;:'',;D``
       7/  - ' ;, '9:''..''"-`    `Jc  yBJ,`u~--:,O-`
       S^  , :-r-`:k'        `      :e`Xz,' =` :``e  
        u,  '  ,=  .e                 ;#Qr '       e  
        t`  `  r:  `y                  KQ^  ? `    H  
        J      :`  ,u                  ;Q-  = |    K' 
        v`     |   :=                  `Q:  |,|    q- 
        |      |   ;;                   Q~  :'|    D  
        ;'     ;   r~                  `Q:  -,o    H  
         ;     /   >-                  -Q>  ,']`  `W  
        ';     P   7'                  :QS  ,-'/  -#  
    iJuuFr/]Jc|d,  o-                  .@R  '~ Q;;7Qv:
    JuuSor|eXeXPXPkK:`,                :@QJ9/Q@@Q@UQ@Q
    JuXdS:~QQQ@@@@QX,^@@QQUuXKqoZtJOQ@Q;Q@QkkQQQQQFQQ@
    kqRNu: HQQQQQ@QJ,:@@@@QQ@@@@@@@NRNo;B@@QWBW#QPXHOE
    FJPyv/,-qN#QQ#NJ, QQ#QQQNDORDUukBQr/R@QQQNDqEeOHDD
    oyuSuKOXEEOooKKX/:;uEKeZSXNQHNQQW@ zEQ@QQQQQQQQ@Q@
    qORHDRRNND&KePZEPZZSuuJtoRQNQQQQQP |ZN@BQNQNQQQQ@@
    eJoHDHRWqkOEyo]vcv7//|7JUQBNNBN=`  -i]ROPkDON&Q#dQ
    etyoo]FJ/|==||||/|>||?7yBBROeyJ/;;;;uJueieZFeiyS]E
    i;?,':;;;;r||||>^;;:;^^eBHDK9EFEKDONEoHWRR&RWdHDRd
    ''.---',:;;;r|?>;;r?|tERR&XHNWWN&BHKkWQQQN#BN#NNBQ
     `       `-',,:;;>/uESoEuZZioU9dduFe9Rd9zNPNNZoyoU
    ''')
    print('''
    You head up the mountain despite your injuries.
    You hope to reach the summit to obtain a clear radio signal to call for help.
    You steele yourself for the journey ahead and bravely continue up the mountain towards its frozen peaks.
    If you weren't already slow enough due to your injuries the freezing winds and snow bring you to a snails pace.
    Maybe you should turn back or seek shelter?

    #1: No, you've gone too far, you can't turn back now.
    #2: Yes, to continue on would be suicide, your best bet is to turn back before you freeze to death.
    #3: Perhaps theres shelter nearby, you can rest and wait out the storm then continue on later.\n
    ''')
    secondPath = input("\nWhat will you do? (1/2/3): ")
    if secondPath == '1':
        path1_a()
    elif secondPath == '2':
        path1_b()
    elif secondPath == '3':
        path1_c()
        
def path1_a():
    print('''                                                                                                                                                                                                                                                                                                                                              
                                           ,K                                                
                                           ;r:                                               
                                          c&S7Ky`                                            
                                          kWBeQez                                            
                                         ?'ORQKQq|                                           
                                        ^ |egDc |                                           
                              -,~'     |  oKWBZ .                     ``      `,,` .-,:;.   
                    ``:;=icv/=;-          JH]aK                               'r,;~::;:     
    ;;i/|Lr;:'   `:?7zLciL|^;^;            ,K=^X                  '           ~||^||;  ',    
    uoJeZoaooooF}]tv=;:,,~  =o|,    ;^     -|'^X   ~` `.:7/       -` '^:''   :7L|/;::~`r*' ;;
    oeoemmmZZSjyot/;~;,~zL:zXjL?,,?>z}|,    |`/e'-,,~^iSoZme`    `'>}7/z/7-^;,ri7/t||r7z|,|i
    XXXXeZoayomoS;:|=zyEucoeJ/F/^^Zmor      J>^  ,:|}oZmPea6`     .|=|:;vtt^*czF]}J]|?^7jSt/t
    XPEXmZSSaeJcuiuoe69PPPyt^;}yzv|`   `,:|/zv;   .;yJy:`:|^    '  ,|,``/J/=cuoSJzc/, . :;|;,
    66EkoJXeSFuPP]juE996o}`      -    ::::|/'' ;``'       ,'`   `~ ,*>||.:,;/}7*;*^;>r=;^;r,:
    696SJoyokq999|*POqmz`    `` `` '-.r  ,F;`   ~          ~;;;;`,::^;*/,,;|}JzSoi/}9qmoqKHdK
    t7z^oqKqqOKe9|uO}ez,  -`,    'r=^.  ~:         ` ,     ,r,; /J;:;?>=zy6EmFuF;zjy^F9mqkmkd
     .*F9DddqZdzo>:`  --:.        -          `-.   v     :,;|7:,;L/|  ']ZmSoXevSy|-:|veeaekO9
    `'` :E];;:::: ,;` vr ` `?/z/|`           --`     ~L;-  ^|c]9/|o>,- -~?ykPmk6PczSjeqqKKDRD
    ':oD^|>;; ';v: -    iHP~      ^--:-`z:     ` ;:;oi;|SSSc>mkL*^:/}v;odkKkya6KOODgdN&W
    `,`::FQ@Qc;}|  :-       '>, ;-   `:Qz|^;;::      -`L ;#D?Jz;}*/iZoXmcFSo|cqj^uDKKWNN&Rddg
    /zoqNQe;    `^LR/,     ^~'7|      /Q#9}Lt `    ,:; `/` :`ruJoXj||,;z}J7i|mXui]oNNWNNgDgQB
    kR@@E ,z` =o9yQQ=`  |Kz.FW;      ;o;~~::#a .,   ,`- ?:~ ;z/>^O=tZ7|;=*ctJgRXKSzoeBNWBQQQQ
    @@@QPz>JymEN6Q;      ;:gr    `-~^WS:-;7zida7/:, -  ` ^^ -;?7?mi|/FRXa^*&QmNKBRoo||BQ#BQQQ
    NQ@#ozEQ@e,r' :?:,i^=yB:   ^  -;HQERN#H::j/KD/:.,t  ` ,  -.JKz/j|io:^/,aQE9BQ#QW7^qQQQQQ
    RQk/qQ&@gy;:^PQQ#v,/Q@`   |  ~zHQ@QQQgo};` /j:;':r;     ;```=/|i;u]tF:;,.KD|;ouQP;yFte6K9
    ''')

    print('''
    You decide to continue on despite the circumstances, the mountains peak must be close!
    You sift through the crunchy snow as you try to shield your eyes from the flurry of snow surrounding you with your arm held out in front of you.
    You can barely see one foot ahead of you, perhaps you should have turned back afterall.
    You can no longer feel your feet or fingertips as they succumb to frost burn.
    With nothing more to lose you try to keep your composure and slowly continue to dredge forward.
    Suddenly the ground below you appears to be more solid as bits of solid rock pertrude from the blanket of snow around you.
    You reach the real summit and you signal for help!
    ''')

def path1_b():
    print('''
    You find a makeshift zipline
    ''')

def path1_c():
    print('''
    It's a false summit, exhausted of both food and supplies you die!
    ''')

def path2():
    print('''
                                                                                                                       `      
                                                                                                  _;'                 ,Z-     
                                                                                               :;oaBH                ;;`j`    
                                                                                            ,;:c@Q@g/             _^-`zB/    
                                                                                         `:::viyQ@@@@N`          _;' 'y@@:    
                                                 -`                                    -^;:U^N@@@Q@@@Q/       ~^;'`'?@@@/     
                                                 tBB_                                  /`y6@g@QOB@@@@@Q.   `,;^`S2Q@@@@B      
                                                 /:QNK:                               -^-QN@Qgj@@@Q@@@@j  ,=-  `96@@@@@a      
                                                 *'/@@Q$'                             `:`Q@@@RQ@@@9@@@@@*`?``'  /@@@@@@:      
                                               |}/Z;Q@@@B;`'              irFF`       .;`QQ@@Q@@@Q@@@@@@e>`: `. `v$Q@@@/`     
                                             ^/v:u@@o@@@@@QQQz``          `/|HQ6OHJ,  `;:6K@@@@@@@@@@@@@>`;`    _Q@$Q@@QQ'   >
                                             /dN9;@@QfQ@@@KQQ@NOBDd>      ?ey^D@@@@@PJg]imR@B@Q@@@@@@@Q:  ?`   `o@@zQ@@@@E `>'
                                        ,:-  z:@@D@@@HoQgc`QXX@#B@@@u_    :;Z$/mM@@@@@@>l6@@@@QNQ@@@Q@|   :   ,B@@@tQ@@@QQ`/` 
                                        LQ@O*:F@@@@@@#B:N/ N@du@#PQ@@@6`` `r;=OQDhOXjz|;;:;,-    `^Pe6       -e@@@@O@@@@g@L^  
                                       `|rqQQ@N@@@@@@@J`=S/=ukOP$ci|?^:,::,-,_::,':||`               '^zdQk/:o@@@@@Q@@@@Q@:   
         :^:::':__::',~-               ,; `k@@@@@@@@@M';;,`     `:''.                ::            .`   -^JW@@@@@@@Qg@@@@@    
        '/ `         `'::',`           :: -`g@@@@#B@Q/;`                             `1/.                  `=]N@@@@@S@@@@@`   
        '//'`;:            ,::::.     ;?   ,;FX|;:'`                    `::;`         `^7akKKdq:`        `''   `S@@@D2X@@@u  `
          -;F]?j1*^` `'`        .:::::/  `^^.                    '`'       :Fe|~-              .oJ~~::,_;}RWWMKa]gQ@@@Nh@@@: -
             ^uKU;ZR^- '^?,``       `;v:::;:` `_;_                           .r/^,,':'`          X#QQQQBNQ#@QQ@QBQ#@@@@u#@@Q;r
             `r;|/jQ@@Qe:-:/RQQ9>^,:~,`     '~7^,,'':;r-_;~,::-                  -                `>/vaER#Q@@@@@@QK@@@@@m@@@u'
    ';:::~`   :z#X^|QNQ@@@@QO>PQNu/|xl*;,`               `';;^/Ou:``''"~:r,'-    _',:-    ,,,:,;=^rr;;:>FH@@@@@@@6@@@Q#Qi/;-  
    z: .-'/^;:::,jgKQQRe@@@@@Qa>=,,'`;Xkcvtjv;,''`  `''    `'~;-?#gKkDBQQQQQQD|-   .:iz]6@D@@@@@@@@@@@@@@@@@@@@Q#XR@@S?`    `:
    'v:` i*>;` `_;]L/@QQQ#Do9#:,:::::;/r?/1hg@@@@Q&gQ@@Qg9OQ@@@Q#@Q@RRDgQ@QgQ@@Qgo]]Zm6DW@M@@@#QQQQ@@@@@@@@@@@QBQ@{v:     ;7\n
     `c#QQ@#S/:?://;'zD@@@@@J^;.     `/dF`;@@@@@@NDgQ@Q@BF:t9Q@@QBN@@@@@@@@@@@@@N@@@@Bh}|>XQ@Q@@@@@QB@@QQQ7:,,,,_;;;;~':y;zHQB
    `   -;?w#@QBQN@@@Dj:/wdz`      .~O@@QQoQQNoc7t^H@Dga''o@@$j/-  `/9Q@@@@@@Q@QRj;,`     _e#QRUvxFH@QqKN,   =oqD6S]cteHR@Q2ef
    ^qQZ;'~~"'~juoL;":|> laaZZO#QQgZq@@Nr;`,.   `o@@@8>_/gQ@@@@MN7;;   -:7atuJ:^{9MBr    f@@@@@NQda/:` -|oua6q@@@@@@@@#NgRKy1'
    9Ne7:`' `':;,     `; .'-`,j@@@@@@X:`       :q@QKo;:jQ@#Oe/;*eEumQ:      `,^uieR6,'?$@QOF/;' ` `;vKQQ@@@@Q@@Qeyhj?-        
     `jD>/x-^^~.`              '___,` :>/oWP``r@Nr'- `i*'`     Mg@@@@@Qv    `  .i9u:'yDz^`     `'vwQ@Qj/*^^?v]Pv/           -N
                '^v-          ,, ;:r^OQ@@@O_':'.   :::     ` -d@@@@QoQ@@/`/2i*K@@@;:;``        '`-` `            `,~~_:;;;:::;
    ''')

    print('''
    You make for the foot of the mountain.
    The winding path seems to travel on forever.
    Eventually you begin to run out of steam.
    Your feet begin to drag and scrape against the unforgiving mountain rubble as you lose more strength.
    You come to a low flat boulder perfect for sitting on.")
    A sitdown could really help you recuperate your energy and give your wounds time to mend.
    
    #1: Continue on despite your dwindling strength, there's no time to lose.
    #2: Take a seat on the boulder and rest a moment.*Have Icepick*
    #3: Take a seat on the boulder and rest a moment.
    ''')
    thirdPath = input("\nWhat will you do? (1/2/3): ")
    if thirdPath == '1':
        path2_a()
    elif thirdPath == '2':
        path2_b()
    elif thirdPath == '3':
        path2_c()

def path2_a():

    print('''
    jZjyuJzczzaPkXajai//ir^|/?=?7i/*/^;;::^/?;:; ::::,:;:'',':;||;;^:~;;r*:;*=;^;;;'  -                                                       
    eE6keoSStuaeZjej}i;*//^r;/i/=?rr|i//>;r//^;' |;:,:;:_;:,::^*^;;::;;;;>^^>/^::;:'`:...                                                  ` -
    OU9qqHXEEo6EPzjev|///zv/^|/|cz/v7//ovz/|zc>  _=r>;:^^;:;^;^^^^*|*=;r^|r=c*?;;;;:,,','-`                                                '``
    DkDW#QDgBK6ePJt7iuuS]77czuJz/zvJu]uu]vujooJ   ^^;;/?^:::;=||vz7v77|;:;>/|*^,-;*//?;:~_,''.``-                                           `'
    RNHRHK9UURKUK6yuZc|v/}ozzSZ//7v=/i//EX6Zac^   ,/zJ/=;;::;|c}SjEeeouu/^;^r>^;;;z|7///^::_:~::,'                                         -:`
    DRW&HDRNQQHXeSuyjSZytu6Uo6oDUouo}vJyPZooZZ;`   i/7=?|?^/u}zooeeSo6Poz//=>>;^;;:;:=>;|r;-:^:,,'`                                         ',
    #Dq&RU9WNRROPX9ERDDHKeeeojXeJ]ujZEEkqKDKZ;`--  :z|||;^/JJzzSaoySSeo|||**?r;^r;;,;^//r=^;/|;;;:'-''` ``                        `   `     `:
    OkqEKR6K&NRqjzZRqR#g#g9aZXe9KPekg&DONKgo,.-` `  yvz|^/ujoucaE6oo9e}ev=|?/|*^;^^;;;/yS]i^=;,~:~::,,-`''````--'              '`;^          
    6UHqUqKNQQ@QQQNQNNQQWDONDgKq6PqU&B#QQK|-' `-    i9z|/=;J6J/uUZSoEj/^|>|*|//|*/^*>^?Pkejv||^;,~_:~,:::,,_,'_::_,,;_,'',-  ;; : ,   :: /, ,
    O9KDR}NQQ@@@Q@QQQQQQRKROH&DKO6KDN#QQR~-.. -`'   `KDKjo/uv/v/JOKDe|||r|||?>>^;::::;^>*>/|7i/*;;:;^?c?**;:::>^^^;;::^;^>>^;^^|>/;|;/;|i/;-.^
    RORNDENNQ@@@QQQQQQQNKRHOQBRHONQBQQWy,'.,` .`,    :Eeouza|zjyO9DZczJz7J||/c===|*;;;;;;:,,~~::,,;/c/|???|r>^^^r:?:>|^=|||/|/|vJz^}zzuu*ojJu?
    RKRg#OWg&RRQQQQNNWRNNQKK&QQgNQQQQQi''.,' -``,.    'vzv*i/oDOKeK6eyJuJj7vz}>**??rr^^;^;;^^::;;/i/||/||>>^|?//;^;^/Jiz*?|i|/icvzSu]taoXX9XtS
    qODD&DQRR&Q@@@@@QBNQQNkgBW&#QHDNP;,,'_:  ``-,:    `'oEejj]XoPDREeuzc/|cvcir;>?=r|r||?r;;^^;;/ic/ic7z|^^=??/jv//zztz*;^|ct]}zJvuoeoeaZzkekP
    q9EeKgWRKQN@@@B@QN&&ROBQNQKEEe9u~,~'.:-``.-`':`    `'yPSv}]zS6azz]]tz]eKXz|>/c>=/uv/tv/^r^^=jo7Jv/////tzvzvvJuzJ/}/|7/vuoSS]vu|vocuZ69qDKe
    Q&jyzJHPU9kokDNQQQQ&RPoeKeZueZ='','-,,```'` ',,  `   .yOeeP9eSuPSPkztzvz]i*v>*j/;=?ivo]/?;;|/v|7utv/ic/i|?*|zjvvtutX6yzzjeuuSauzSPPPP9KHOa
    PaHRRkXSjSo/?ZqEo66eaoUP]jkoz~''.,:`` `,` -';      ``tQWNWk}uSXj]tyeuyKe/t7SZ}oojc|vc]i/|JySutj9Okuvc/cc//z}kkzok9oi}zuPyEPqkXEke6jZK9DU
    Q#QBQQ@QDXovz|/zJU969DgD&&U?,'',-,:,`  -,` -';'       `>KoyJj/ziJj/?|||//^|/?|/|7r|*/UHSoryPuouuz77zvcuv?//cvP9uSqEZuSJaXuoEPSeZee96qZKgK
    Q#QQ@@QH96KPttJvvuuKKR6ej]:'',-'~:`  `-, `-':;        `:Zovcz7z]uaoeoo]v//|=>^>=^^^;;;^^rtjORRDv7|/czSoo}tJtZHeekPoeeS]tkykEo6P6RRKKUKRD
    KN@@@Q@@@@@@Ngo9HDUURQQUz,,,'',.',:'`` `.,  `':^-        `'czyjzvJooaPUZe||7///r|r;^^=>|^=;~~_:;i>//|/zvv}SyJzzzDeDEayt}XEHD6kPqHHDRP6NKU#
    R9&QQQ@Q@@QQQNRtt|;>/7u;'',,'',:,``  `',```-,;:         ``^]X6&#QNDaojS};|z}/c]Sayue]J/|///^r>;||tutzuou]]J]k6&DRyEeXP9KkqqZXekqHKePKNKH
    WNB#WRQQeXUgWo}z/ouJJJ,,,,~_,-'__;-` `-'',  -',:;         ```zB#9ESujUq]Jt/uuJv}]jjED&#gNR9X6eUZjj7zuuv/}zoqkUUekDO]zX]oeP9Kke69gNWgQ&&NQQ
    KqDROKDRSzJi/cJ7|oP9*,,,,',,.-,:;,`````-,,   .,:;,          ``=eeKeoaUoeUKUoOWqKHROK&NQNNRNNRgWR9UPaoZjZuja9qKDR&gNRRN&gg&Wgg#NN#BBNgNN##N
    OD&&&qeZi//J//|/|oo;'',,-.'~;:``````','  `-,::;     `     ``~NQQQQQQQQQD/uNQ#NQQQQN#gW&NRRNDDD9ouZkooyzi6Do/z9WNRS,.`-=DH&&RUkEU6K96UEe
    yJueyjz|/|cz}]y]//,'',,,~,``'_;;.``  `',,-  `',::;'            `,HQQQQQQQRK==PDKKDo/>*vk&HKOk6e9BqP]jo^'`JEX~-   `uJ:` - `;//?*;;;:::~,,,'
    tuo7z/|/Sjuuvi?/;,,,'',,---,;=,`` ````',-  `'~:;;^`            `-|NBQQQQ&D?^oK9c,''_`  -z&&WRkH&K}>^;-   ```''    . ...--`-``            
    Oqy}]J]jo6Jvt]/,,,''..',--'~:;;``    `-.,-   ``',:;~             ``'jDNQQQQ^/XP,-,,,_:    .z/;,:,,~_:_,,`                ` ` `    ` `  ``-
    qOHkKQOSkj]o7:''---,,'',:;.`      -,:-`   `-',:;`     ``      `` :SNOky=>|;,:::::;` ``-.         `         `` ``````````             `
    QQQQQRUeku7|,'.`-.',:,.',:::;'`     `',,;-`.'-`-'~::,           ``-`---       -````      `` `       ```````            ``                `
    QQgDeaoZ67:',,,,,,:;~,,,,:;^:--`  `',,,:;.`  '_,,_::;`       `     `--'`  `  ` `   `````                                  ````       ` ```
    ^?>;;:,,,,,,,,,,:;;_,',~::=^'',,'--'~:;'-  `-,::;;;,``    `-'`     ``-` '`                               `     `       `` ````-` ``-``-`
    ''')
    
    print('''
    Continuing down the mountain you feel great relief as you see smoke in the sky nearby.
    There must be people nearby!
    Sure enough as you continue to hike towards the smoke you spot a group of campers huddled around a campfire.
    Shocked to see you in your condition the campers rush over to assist you.
    They take you into one of their tents and begin to administer first aid to your wounds.
    You'll live to see another day!
    ''')

def path2_b():
    print('''
'"'"'...--------````````````````````````````````````````````````````````--..---....""""'',:
'""""'..------`````````````---`:*|/?;:,,''.'.--'::|v7??r*r,-`````````---.'""""''""""''""""' ',:
'""''^$#daz*_'----```````-':*v2Z$dPXd$jouzxJtF}jZoSmkONMwooORdX//>ijyxi;:,''?v;',,,,,,,,,~:
' ',,z@@#d$kR8PZv>,'..;luoePOKqgQOojUwjv/*|>|///cvivPeafLJPqPXmkQQ6vzztZq&PjyfL' ',,,,,'',~
.'""""':udRDdOMN#QQQBNKD&RR6kRk]x9eu}jPjr7L//|>r^^;;:*vzi/ioqZxvzSK&jzzxzF]dQ}mvo^,,,,' '-.',
'""""' ',;7XOdqmX6kUM&6OMkwORO]zyS]vt2Xu2Su}L?r>r;:;^?///vXPSvLLz]u]vLlJfmomQgRgQ#m:,,,'""""',,
.-......',:*cvvlv}]zz2UzyZtL//|>//l}wmqmj]/|?|>^^>>;^?cfoyJ|||||/|/|cj2OKKO#&DdR#D/~,,,,,,,
..--------.',:;/vz]]j9U///||||?>||i7j$deF??|||>^>?^|/vz}tv/>^rr>/iv]ue68ggBgKmjZOQQj~~,,,,~
'----------....',,_:;;?|*?/|////||/i}oKetc/||||>/7//ii//|r;::;>^^L}2fwgKDNKwPzrr|kB6:~,''.'
.------`---`--`---.'';rL/|??r>*>^r>|/ikHZ/|/>>;r//?||?>*^^:_,~_;;|ezFoPkU6y]cv|cvz}mc:,.-``
.----------``-````--'',^/zJi|?*>>>>|>>oDPv|>^;r>r^^>?/x]/^:::;:;^/zvvSSjyu|*?i]HQMyzvi:'.-.
..-..-----```````````-.';cuc77/|?**r^|]]v/|^^^r^:;;*>rr//i|//|||^rr/jyv//*^>*|ce#@@&ayUZ:,'
' '.---`--```````````--';l/cc/?>^;;;;:,'---`--',_::;;^;r>r/|^;;;r;::,,,,,,' ',,~:/zoX}]?'..
'.----------````````---:?//>^;;;^;_'-``` `   ``-',::;;;:;:;^^;;_,'------`````````---------
'....---------```---':*i/?r;;;;;,'-```         ```-',_::::;;:;^;_,-``````````````````---.'.
--.....-----`-``--,>//vi>;:r;~'-```                ``',::;:::;r;;:'```````.'````````-----.'
 ' '.-----`---.---.:^>izv|;^:'-``                      `''~:_::*;::_'````````````````----...
   ''...--``---.,:^^L]c|^:'````                     ```-,:::_|v:;;_.`````````````````--...
    ' '...-------.' ',:;>/eL??;,-`````                   ```'_r;::>m/;;;,-````````````----.''..
     ' '.'.....--`--.''rv//ao7|^_'`````````                ``.;eL;;|Scv]^,''-`````````..--..'.''
'""""''.---------.',vdtiySOXJ;'`````  ``````           ```.:L]||uzJkv*~'.-----`-----...'""""' '
'""""' ''.''...-..',/#M}tuOgf?'```````````` ```````````````.':r::;qgDz:''-----`-----'.'""""'' '
'""""''""""''""""''...'':vZ}?_~_~'```````````````````       ````````'~|K@#J,'.-----...'""""''""""'',,
,'""""' ''......----' '.---`````````````````````````````````````-'~/6HZ;.-```---.'""""''""""' ',,
,,'""""''""""''""""'..------``````````````````````````````````````````-.' '.------------..'""""',,,
    ''')


    print('''
    You take a seat on the hard surface of the boulder and lift your legs up to let them rest.
    You feel a great relief in your sore legs and thank yourself for taking this rest.
    Suddenly a loud snarl imminates from behind you.
    Quickly, you turn around to see a wolf just feet away from you bearing its fangs!
    The wolf looks rather thin and unhealthy as you can see its ribs pertruding from its skin through its thinning hair.
    The rabid wolf lunges at you with its howling jaws.
    You remember the icepick you found in the abandoned cabin earlier!
    Hastily,you reach for your pick and swing in the wolfs direction, closing your eyes tight and bracing yourself for the bite.
    *CRACK*
    You hear a loud yelp and then silence as your pick connects with the wolfs skull.
    You can barely believe it, you killed the wolf and without a scratch!
    You proceed down the mountain safely...
    ''')

def path2_c():

    print('''
Licclllciv{icv/ilLz777/|||??????>>>>>>>>>r?//?=>>>>r
;;^>*=?>L1luaK2i||1/tuzLr^^^^;;;;;;;;;;;;|ie#Dei>r^^
vz1{]1zcv||]FjJezSSuRLlz/:"":::::;;;:::;Lu{E@@B#i^;;
,,~::;;;z]i>^^/zfEgQK]aur' ',":::::::;*7SdmXQ@QQ8|;;
' ' ',,,~:/FjjyzizoDDu^'""""' ',,,_^io$6y]9guK@@@QQ#9P
' ',_:::::";S}/lFXDD*''"'',:^/fPgQQQQ#RHNDFDQ@@QQBQQ
::::::::::_;z?>tj6Dl,,,:/eH#Q@@QQQQNQBWDDeSO@@@QQNWQ
;;:::::::::r*r/FZOO;~:FqD6eHQQQQQB8HRQQNZ1XQ@@QQQQNg
:::::::___:/;;LXR##?;Z1|i6NQQQQQQBRKD8KuzSD@@@@QQQQ#
""_",,,,,,:;-'mNBBO;*eSL/ZQQQQQQQQ&HNQNK9R@@@@QBQQQQ
,,,,,,,,,,;_:SMBBNm;/ukKD&##QQQQQQ#N#QN#Q@@@@QQQ@@QQ
,,,,,,,,,_=:"JODPkaimqXRDORMNNW#NDDdN#QB@@QQQQ@@@QQO
,,,,' '"';cv/|tLFuaXk6kai>/72aqD&DdODBQ@Q#NQQ@@@QQND
' ''.,::',;^|zc]SjemyzzFFvrrcSKRDHDHD#Q@QN#QQQQQ#8##
--'lgBv||viiiz|z1/>;:;/JSZLr|FKHDRW#QQ@QQBgDg##WRN&D
-`^BQvz7/L/=;;:^^'',,',;=/|||fq8##NB@@@@Qgd$DNQQQ&D&
   ;PP|;r;*:;;;r^;;;;:,` `';/JH#QQQQ@@QWHOdD#QQQN#QQ
    ,}RO96dqR&NNWNRko]/^,.';/SWQQ@@@@QNMHDN##DN##QQQ
`     ,S6K#@@@@@Q@@@@QDhz^,^Lm#QQ@@@QB#BDNQQQQQQQQQQ
`   `r9QQmhDBDQNdDhSSoyeOu|/{jDQQ@@QQQMMRQQQQQNQQQQQ
   'JONQQQBQQeQBef'    ,QOPXPXO@@Q@@QNODN#RdDd#@QQQQ
 ,veoaXK&QQ@@@Q@Qi`    ,Q8O6RRDQQQ@@@RODRD&&9SSOQBHe
:OgBQ#RddNQ@@@@Q@f     :@Q9&QQ#NQ@@@@Qg8WRNQNE$kPaee
ZhDQQQ@QQQQ@@Q@Q@u     ]@OMQ@@QDBQ@@@@QQB#BB@QOqkmeK
qRN#QQQ@@@Q@@@@QQ?    :QBg@@@@@QWRRMQ@@QQQB&Q@gOXwm6
NQQQQ@Q@@@@@@Qg]:``` ,NQQ@@@@@@@@Q8kdgB#NHS{R@BheP6q
8gNBQQ@@@@@QNv,.-','/gQQ@@@@@@QRo/;,'_;;:'``'fXeXhPk
NMHKO6K8#QNa^''.-./qNQ@@@@@R7;'``````````,;;?yaXwm$H
DSSSj{zF]y/,,'"'',/ER#B#Nq*-``---...--``/OdD8N8RRg#Q
mf2eju1/:,' ',,",,',~:~,'""""  '',,,'',:;/]2PRQQQQQ#QQ                                                    `-'~::,,;=/Lztu]zz|;`   '` `'-`
    ''')
    print('''
    You take a seat on the hard surface of the boulder and lift your legs up to let them rest.
    You feel a great relief in your sore legs and thank yourself for taking this rest.
    Suddenly a loud snarl imminates from behind you.
    Quickly, you turn around to see a wolf just feet away from you bearing its fangs!
    The wolf looks rather thin and unhealthy as you can see its ribs pertruding from its skin through its thinning hair.
    The rabid wolf lunges at you with its howling jaws.
    You close your eyes and brace for the end, throwing your hands up in the wolfs direction in an attempt to protect yourself.
    You feel the wolves sharp teeth sink into your bare neck as you slowly lose conciousness and drift away.
    ''')

def path3():
    print('''                       
';;.,  i^  ,,      ,`  ~:  '~'^/*,-:~::,:F,;|=.`*|.~riz/r*>r:                                                              ````'
  :  - /,';;^ -   :`--:~:;,::,^*L|*;`  ,;L;^:' ,/  `'**/ :z^/;                                                                `'
  ~ '',=:: /;::     `~ i7/|*|:'``       :};'^: -:;==?/cv=^/;ii'                                                          `    ` 
      -vi;:t.'  ,-';;^;::r=>|;;`,'   `-:^v/|>|:';^;>//uu}7i|v/-                                                               ''
  `   ;, >,c*|/>||i>^'r*=L/*r~^;*^:''- -|i^>;::-`':~.|ooyFjuyz7,?`                                                            -:
       , /=tL'= '=:; ,Jv=r||,;r*ivLi/Jy]]' `:    ` -':r:::;;c/JFz/-                                             `            `:;
 `     : :/t|^: :''  ,:*: ;~.:iJvzv/7zouu,,--  -:;'`,:o=;,` ` `-~`:r>=i/^;::~,              `-               ``'`` -  `   `-``,,
>^,    '- >}r=/~/`/:;=z>^;r~||/vvt7z/;>v;'          ';X/||;'``,,-   -. '-,::;,iLizi*^::'    `         `      ```-''.``   -  `,;
|v::;,  ` ,o`: ;~,|  ;/^>,::>//rz/tJutZZm`        ` -,L>;,'::;:,`` .,-``-' '`-`;^;`:;^''    -        `      `'..,,,,```-``''``-,
|L/i:-;:--,i/|,=;v:',r^|^'=^-;*/uttF}u]Ju `,-,,     -:Z:::;^^',: `,           ``;,''`` `` `'         `   ` `':,,,''--.,,,,,.`-'
=^';/|:r|^>ti*>/]*:,',:,,,~;|7^zt]oujjF]:       `-   ;o*=UOe|,::  ZHKZZtz^;~  --', --`  `,'':  '`   `:-   ` `,,,.'``--`''='',-'~
;>:'|:/:::;]?;/zzcr?;;,*vv>L7]u}yt}Seyu}/    -  ::,;^^K?;J- :     tc*}SEqdRNNQNqao//v/^',--';``..  ```       `````--',','-,,'.',
' ,:r}cv},:tc:/zri|?>^*r>//iJ7FiuF}a]]ze.  `;`  -`  -;7':z``:     ''~:^?izL*}yaoSSyeEKDg##QDOquou?r;?;'  ``````-,'','',:,':~,,:
i|v?^,:.v/:v|:v7^^:,,,,iuvzjt7c}tjZZZSDz        ',,';:| -`  ,`   ,*,'``',,'':;,?/irLv}Jv*vzvzSX96KDD&QQL:'-'`-'',',:,'',:~':,,,:
|;;?/=r;:|zZ*zv;,~`,,::Jv//7cuoaXXoj6Xe|     -`',:;:,:;         `:mRz:,',,''::;;:;?*;;:;^/v|r|z]J7JmoSD'',:~-,,,,~::,,,,;:::::,~
'`,'',,r|:oPmFL:;^;/i/vS/i7?SSamFyoXmZX|`  `- -:/zmkvc|=,        -RKBQNi,,'-;'   `,;^::':::::r^^;r>=?=;,,,',,~.'':::::'::;,;:::;
,:~,,,.`:i6OQz;^//=|/|/|vytLS}zzFuamoo/=;   `-   `;;;>L;,'>:~::|;`uSmOKORu: `:'  .`` `:-;, `,,'`'-,,`,:;:;,'':;,~;::::,:,::^r;*:
::':::-,';OZZ;/u/|/=icLz7youotjF}]ukKz;''        ';^':',`,''`-    zdRN#g#QQ#i','          - ` ` `'``-``- `~'`';:::;>Lv|L|:^**^|;
:`'~::-::;]Ez}c|r^=|///v]ujSyuc/|cUDQz--  `       ',~''~r^ ;;K    ^zzuje6ODWWQ>-:`;kDqkEyzvv||v///;*>;~-:,-`..:',:;v7z]}v*;|?L/>
,.::;;',;;=cy;;=?=|//|||F]uoueaFeKgQQ]',         -|r>;^;^~  'y   -;]JoakdDWQQQ; #Z:|Q@@@QQ#RR|rREDWN#QkmyPXZ|rvz}]|;^|tt7c*i?L|=
,':;*;'=r:;*/;;^=rrv/r?|i|vmZZjtveZe6  `          :;;,,:`* `:6 ;,`=m}tSSuEeUORc DQQQ@@@@QQQQQ^:Q#DRD&Q|;,^7|;^:*^>:*|Lz/rL//r|||
'.;^*;,*r,:,^;^^|LJSSJL*cvjPZFL/:|r^r              ` --. ;  ':    ~yiiFuaXX6qOv qOQ@@@@@Q#QQQ|`g&DO9P&/,:=v>r|*?v:'|?|/|?//|//uF
:'=>*:;|='';|rr=|i}SuFt*iJ}Z]/|r~r?|r             -, `',`r  c}    ,k9KKUUqK6KEj ^ZNB@@@@QNgDDz &Ng&RRg^-`,::,::;;:`::;r^|*/t|r|>
::|/*,:?r `:||||/vueyyzLyzFvuFi;:?/|*             -',,,' ;  |>     Jr;^^=||/Juy |u&#@@@QRR##NE gggR9mEr' ::.~:;:;; ;rL/||/rc|r:*
:;/L?,:^' ,';r|/*=]Z}]zvEoyzL|Lz:L//|               ::r; ;  :'     S6kUUE9UE6dP |mKR@@@QgK9XEu ZPeoaakv~`r>r ,,',, ':,'','',.''
:^?|>,;r,`~;7/??|/zJ/|/vauyzyZeU:oFXZ              `,'' `i|?>^>- `~/^:;;;^^>/Lc ;zPU@@@BH9KmmX S6EmmZo|;`^:?:``--- -.--'-'',;|L
/Li/i|yJ  ';jiLrryoFJFuuooZXEdoo'Jtku                .`  ; `      ^aXoutz}JL||/  /}v@@@QEaS*|* ;=*>*|v;- .'`'/^=::`;,` ^]z/*^;:,
|/icvzmE`,:;c|/LoUH6aFZEuJuFFzc;vuvu:        `'``,:;~.- -~   `` `-|u::;;;^;^^r?  ^r^rrr*r77r;; :;::,~:   :;r>,,,````   `.`.,''
Fz|=r*|;,*::;:::,::;~''``      -^k>:,:`  :`::;:.';Lvvr^|^r:/9azv?:>-     '',,;,-ivi/vvi/Jv7zc^77/izooJ^uyajomPP6yv-      ```.'-
                               -:' '     -        :/L^;;;^|||;,,^|^,}kgQQQQQQ&:~,:z##QQQQ@@@D^;]N&kEj7::r|LFjFz/>^:.-`    /     
                                                  ,::,`-   `';^^^;;, `':,|tJSv   ,o&DHqZ]vjti//|;':;,,-                         
                                                                                 :^::,'.---                                     
    ''')
                                                                                                                                               
    print('''
    After searching nearby you find an old abandoned cabin not too far from where you fell. Maybe someone is inside?
    #1: Walk up to the cabin and knock on the door.
    #2: Break into the cabin.
    #3: Look around for a different cabin.
    ''')
    fourthPath = input("\nWhat will you do? (1/2/3)")
    if fourthPath == "1":
        path3_a()
    elif fourthPath == '2':
        path3_b()
    elif fourthPath== '3':
        path3_c() 
        
def path3_a():
    print('''
                              `FBWv`                             
                              {@@@@6                             
                              P@@@@Q-                            
                              *@@@Q:                             
                         .;|^/#@@@QKoSSv?:`               ~^     
         ,-        -:rLmB@@@@@@@@@@@@@@@@@@QQNKeZemeZaSSeN@Qevo?`
       ;UQQdOdD&NN#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QQBW9uc*;,`  `  
      >v,':^/toePkhmPHNQQ@@@@@@@@@@@@@@O7vLr:'```                
                          K@@@@@@@@@@@e                          
                          >@@@@@@@@@@@:                          
                          '@@@@@@@@@@@                           
                          .@@@@@@@@@@@                           
                          ^@@@@@@@@@@@`                          
                          e@@@@@@@@@@@,                          
                          #@@@@@@@@@@@/                          
                         'Q@@@@@@@@@@@S                          
                         :@@@@@@@@@@@@Q`                         
                         ,@@@@@@@@@@@@d                          
                         `B@@@@@#@@@@@]                          
                          N@@@@O,Q@@@@|                          
                          k@@@@/ r@@@@}                          
                          7@@@Q' `N@@@]                          
                          i@@@a   /@@@k                          
                          u@@@{   'Q@@@,                         
                          y@@@c    X@@@_                         
                          j@@@;    /@@@,                         
                          O@@#`    ?@@Q'                         
                          9@@j     .Q@@^                         
                        .a@@@z     `&@@L                         
                      l@@@u*.      r@@k                          
                       ;/*,         '@@@,                        
                                     ;/:                         
    ''')

    print('''
    The cold is too much to bare you're about to fall over and die!
    You approach the cabin door, saying a silent prayer, hoping for someone to be inside.
    You knock on the door several times until an elderly man answers the door.
    He takes you in with open arms.
    He saves you and is able to help you to safety the next morning.
    ''')


def path3_b():
    print('''
                                                           .ikPDdr   
                                                         `^fZoPD@Q   
                                                       -|zu{1kRB@a   
                                                     `;F/{uSHgQK:    
                                                   -;{]/fPXgQo'      
                                                 -;//vjhHH@a~        
                                               -;>|vjwKNQk-          
                                             `:^r/jhqgQ9,            
                                           -:^r/FmUgQX,              
                                         `:^^|twKgQ6_                
                                       `:/r^JeUgQe,                  
                                     `;;/rcemqQX,                      
                                   ':/;cvu9KNj.                      
                                 :o6FcujaR&f-                        
                                 _|/wODgQJ'                          
                                -:LuS9Q@:                            
                              -;zoo:-,:~                             
                            -;LuF:                                   
                          -;/]{:                                     
                        `;/t1:                                       
                     -:|{c'                                          
                    `:?1c,                                           
                  `:*z/,                                             
                `:*z/,                                               
              `:*1|'                                                 
            `,>J|'                                                   
          `,^f|-                                                     
        `';z|.                                                       
       ';Lr`                                                         
     `:>:`                                                           
    -~.                                                              
    ''')

    print('''
    You break inside to find an icepick and supplies for a fire. You live to see another day!
    ''')

def path3_c(): 
    print('''                                        
                       -:'--`----``               
              `:|`   -`::  ``   ` `.-`            
         .rFk#QQQOL-`;.;   ``,,`     ```          
       'eQ@@@Q@@#>``|c.`   ``'-L/i:  `  `,        
      `R@@@@@@@B'   r9r|/>`  ``~#Q2^.`-`  '-      
       N@@@@@@@1Xj~O@Q&@@@Qv??/>';F;'   ```-'     
       ,O@@@@@@@@@@@@@@gQ@@@@@@@@j'`{QRo?` ``'    
        j@@@@@@@@@@@@QF  ';w@@@@@t,` 'Q@@Ql  ``   
         ,r#@@@DeDKtL:      -y@@@@@k- 'Q@8L'  .   
            ;jO;;_- ';8Kmj]FoE&@@@@e^, ,@@Q:  -   
              >/vXzo?e@@@@@@@@@@@@@QrL; e@@:   `  
             ` _:o6SwgextfoUQ@@@@@@@@@kmQ8u^,'`-  
            _`     `         ';q@@@@@@x       .   
          `': '|/r>;:;''.,'' .,;}QQ@@Q'-`,/q= '.  
          -;R';,?>./u$QQ@@@QQQ@@Q@Q@@@QQ@@@Be '   
          -i@Qy/`z:'  `/Q@@@@@@@@@@@@@@@@@@Q:-`   
           `*Da*,;Q@QNK;-Dk^7XN@@@@@@@@@@Qy,'`    
               *H&z#@@@Qi'PK;   '^LzLvaX|:''      
                 .r^lH@@@N:~9Q1,   ,,',,',:'      
                     `' N@@e:;Q@gv,               
                         ;H@@H,K@@@@#?            
                           :vBQz;jSEN^            
                             q@Qz   -             
                            ,j'  ``               
                            Z- ``                 
                          -;'/r                   
                          r^*'                    
    ''')
                                              
    print('''
    You've broken inside to realize no one is home...
    Hurt, cold, hungry and alone you freeze to death with no supplies for heat.
    ''')
print('''
You approach the foot of the collossal mountain.
The air is cool and the sun is high in the sky.
Peaks reach out from the behemoth touching the stratosphere.
The last two years of soul searching have led you here.
''')
print('''\n
                                                            `iQa                                                                  
                                                           ,N@@@,                                                                 
                                                         'O@]N@@e                                                                 
                                                        J@H,&@@@@^                                                                
                                                       ]Q/  ;Q@@@@v`   :w'            `'                                          
                                                      rj-    .Q@@@@Q^:e@@Q;         `z@@d`                                        
                                                    ^e;       ]@@@@@@@Oz@@@/       ;Q@@@@Qv                                       
                                    `,r>u|       :d?        `Q@@@QQ@F  ;@@@o-   'd@Ov@@@@@F                                      
                                 ->Jyur` a@i:   ;Sz-         /@@@@>      Q@@@@hiS@@j '@@@@@@,                                     
                             'r1SPz'    /@@@@QDQa'          >@@@@O`     ;@@@@@@@@@/   @@@@@@#;                                    
                          >ek@#,       'Q@@@@@Q.           ^@@@@@Q:;  ,9@@@@@@@@@i   -Q@@@@@@@g|`                                 
                       `xO/_Ny`        q@@@@@S`            w@@@@@@@@aq@@@@@@@@@@$     `xQ@@@@@@@@{'                               
                     :}u,   ~KQ@Q;   -X@@@@Q^ :O^          ^@@@@@@@@@@@@@@@@@@@R`       `B@@@@@@@@@E:                             
                  -vh^     ]@@@9'   'N@@@@Q''DQ;          -Q@@@@@@@@@@@@@@@@@@@^         /@@@@@@@@@@@Q|`                          
                ^K#^     ~d@@R:    `O@@@@@R:BX'          'Q@@@@@@@@@@@@@@@@@@@Q-  ',     =@@@@@@@@@@@@@@]'                        
             `/Wj;     ^B@@@h      f@@@@@@@Q?            q@@@@@@@O^Q@@@@@@@@@@{  `#Q     h@@@@@@@@@@@@@@@@q'                      
            -X/`    ,uQ@@@@v       o@@q/7F;           .zQ@@@@@@Q/ =@@@@@@@@@@F   ?@@'    ;JP@@@@@@@@@@@@@@@@F`                    
           ;{- '7xiR@Q7_/7:        F@,             `/O@@Q@@@@@S` |@@@W*rx7i^`    }@@,       P@@@@@@@@@@@@@@@@B:                   
          L; ^D@@@@@j        `|;`'2Q}              ;|z/`^Q@@R,  -QQZ,            H@@:        U@@@@@@@@@@@@@@@@@@Det|;`            
        ,O: ;@@@@@D,        `Q@@@@D'                   u@@@U               _,   ,@@@@:     `U@@@@@@@@@@@@@@@@@@@@@@@@@Qo,         
      -x@@QB@L v_'          :@@@B}'                   /@@e-            ,rvWM-  `g@@@@R     R@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7`      
     ?@@@@@k-               ^j7:                     >@Q:      `|OW##Q@@@@@F  .D@@@@@{    e@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@U^`   
   ;N@@Q@@v                                         ;@g`     'o@@@@@@@@@@@@@ye@@@@@@R`   7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a' 
    `?H@D/` -                                          :Q{`    :K@@@@@@@@@@@@@@@@@@@@@@@@@QgB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@N
    URXL`                                             `/'   `7dQQQQ@QQQ##ggKEamUHUhZoRHPouyufjjPamo$eo7Fcvx}jjJu}mPmqyZPPejj7r:,,`_,`'
    ''')    

print('''
      __________.__             .____                   __    __________               __             
     /__    ___/|  |__   ____   |    |    ____  _______/  |_  /______   / ____ _____  |  | __  ______ 
       |    |   |  |  /_/ __ /  |    |   /  _ //  ___//   __/  |     ___// __ /__  / |  |/ / /  ___/ 
       |    |   |   Y  /  ___/  |    |__(  <_> )___ /  |  |    |    |   /  ___/ / __ /|    <  /___ /  
       |____|   |___|  //___  > |_______ /____/____  > |__|    |____|    /___  >____  /__|_ //____  > 
                     \/     \/          \/         \/                        \/     \/     \/     \/  
''')
StartGame = input("\nDo you dare climb the Mountain? (Y\n): ")

if StartGame == 'n' or StartGame == 'N':   
    print("\nYour missing a trip of a lifetime, maybe next time?\n")
    quit()
elif StartGame == 'y' or StartGame == 'Y':
    intro()

