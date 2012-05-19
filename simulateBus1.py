"""
This script is to simulate Traveller Bus #1 driving on the Red Route
"""

from random import randint
from time   import sleep

import pointClient

redRoute = [("-79.4446039037487", "37.78697523876900"),
            ("-79.44484779572560", "37.78713601977000"),
            ("-79.44506589150060", "37.78728395149280"),
            ("-79.44530898318890", "37.78737440461070"),
            ("-79.44541477709620", "37.78737517576510"),
            ("-79.44551312906060", "37.7873764716009"),
            ("-79.44652111624210", "37.78705957151530"),
            ("-79.44669002677490", "37.78691092332740"),
            ("-79.44450898322490", "37.78529348334150"),
            ("-79.44372359224060", "37.78469976620850"),
            ("-79.44294440475950", "37.78413272452300"),
            ("-79.44214519854050", "37.78360115803030"),
            ("-79.44081043717270", "37.78267184267190"),
            ("-79.43966763752100", "37.78188327143860"),
            ("-79.43845049693450", "37.7828514531376"),
            ("-79.43926077846030", "37.78337243061660"),
            ("-79.43988491259300", "37.78378474430910"),
            ("-79.44004007802150", "37.7838804247198"),
            ("-79.43917589992130", "37.78466216216280"),
            ("-79.44017503283310", "37.78538187337720"),
            ("-79.44096571432300", "37.78593783382550"),
            ("-79.44077670941830", "37.78617164841030"),
            ("-79.44065502962980", "37.78640940328760"),
            ("-79.44049675256490", "37.78693015544030"),
            ("-79.44032520326220", "37.78723972044850"),
            ("-79.44008494423350", "37.78751287991620"),
            ("-79.43964706097780", "37.78780624040270"),
            ("-79.43906596405510", "37.78812222855580"),
            ("-79.43871419410590", "37.78825610154620"),
            ("-79.43730957042120", "37.7887432739055"),
            ("-79.43599168360740", "37.78924516759890"),
            ("-79.43504084502340", "37.78955074685050"),
            ("-79.43435697831250", "37.789619137682"),
            ("-79.43352554448960", "37.78969157360550"),
            ("-79.43306859598540", "37.78968722635860"),
            ("-79.43240670913450", "37.78961974317560"),
            ("-79.43213192533620", "37.78959795855230"),
            ("-79.43187242769160", "37.78957350818560"),
            ("-79.43150625322960", "37.78951534124350"),
            ("-79.43122987773250", "37.78945700010510"),
            ("-79.43087838038910", "37.78944503917200"),
            ("-79.43047748250180", "37.7894785845218"),
            ("-79.43003863179370", "37.7894973518407"),
            ("-79.42977611300600", "37.78951812972140"),
            ("-79.42947937369390", "37.78957314111630"),
            ("-79.4292079560869", "37.7896587643263"),
            ("-79.42901275021670", "37.78975305523260"),
            ("-79.42878500353120", "37.78992017401030"),
            ("-79.42865435708190", "37.79007468625050"),
            ("-79.42853921970510", "37.79026838779750"),
            ("-79.42844952420770", "37.79054150089680"),
            ("-79.42836258025630", "37.79073644574430"),
            ("-79.42817462000920", "37.79105462512260"),
            ("-79.42772244129490", "37.79148842414190"),
            ("-79.42723309874090", "37.79187822921950"),
            ("-79.42596235593000", "37.79294227076320"),
            ("-79.42649424123370", "37.79307590673090"),
            ("-79.42727964043100", "37.79322481651250"),
            ("-79.42755994386890", "37.79326739986240"),
            ("-79.4278437807006", "37.79336280942960"),
            ("-79.42817917270220", "37.79355407615140"),
            ("-79.42848702078790", "37.79375623616480"),
            ("-79.4287988890828", "37.79393134830450"),
            ("-79.4290988204903", "37.79405759962970"),
            ("-79.42950577239640", "37.79416538171150"),
            ("-79.43070613215750", "37.79441853982800"),
            ("-79.43125750942390", "37.79451300800190"),
            ("-79.43178920836710", "37.79455969213180"),
            ("-79.43218535994220", "37.79460677439000"),
            ("-79.43256151585620", "37.79461445199070"),
            ("-79.43301924834690", "37.7946183099122"),
            ("-79.43343720218500", "37.79466451720620"),
            ("-79.43437394530300", "37.79472322096150"),
            ("-79.43510122229090", "37.79480302893880"),
            ("-79.43336403624310", "37.79464475481920"),
            ("-79.43271880748960", "37.79461490203670"),
            ("-79.43211481345110", "37.79460529219820"),
            ("-79.43163145499820", "37.79456666109400"),
            ("-79.43152600528400", "37.79459833269810"),
            ("-79.43149419017420", "37.79467148195330"),
            ("-79.43150736995760", "37.79476256317410"),
            ("-79.43151434207060", "37.79487079325910"),
            ("-79.43150458250900", "37.79505626119010"),
            ("-79.43150008685210", "37.79524342216650"),
            ("-79.43148500110230", "37.7953828884119"),
            ("-79.43148702510610", "37.79592851833590"),
            ("-79.43150526013650", "37.79636001950770"),
            ("-79.43153668937060", "37.79671674379730"),
            ("-79.43154015920920", "37.79722984982700"),
            ("-79.43150375685770", "37.7976525702874"),
            ("-79.43146229430760", "37.79808472410500"),
            ("-79.43139548457230", "37.79855674366050"),
            ("-79.43118264848620", "37.79910834376120"),
            ("-79.43080912630400", "37.79979446945450"),
            ("-79.43043959639690", "37.80035236113980"),
            ("-79.43003093177020", "37.80096074174660"),
            ("-79.42988717024610", "37.80121007079720"),
            ("-79.42961498986750", "37.80142042956640"),
            ("-79.42923029493860", "37.80166875201900"),
            ("-79.42888054305560", "37.80196342272900"),
            ("-79.42876288313790", "37.80208579121810"),
            ("-79.42851933573050", "37.80196301051160"),
            ("-79.42820215144290", "37.80194632665800"),
            ("-79.42792960355030", "37.80194442327990"),
            ("-79.42781078683220", "37.80194889547150"),
            ("-79.42768645211030", "37.8018961441565"),
            ("-79.42761526981230", "37.80181748423100"),
            ("-79.42759081297180", "37.80175824996270"),
            ("-79.42760640098850", "37.80166185374050"),
            ("-79.42760167813580", "37.80153250708200"),
            ("-79.42761624129070", "37.80140095573880"),
            ("-79.42763866458060", "37.80127847155770"),
            ("-79.42764909233430", "37.80114985991870"),
            ("-79.42764231348900", "37.80103987593550"),
            ("-79.42762163935230", "37.80092164331880"),
            ("-79.42769507133460", "37.80081211697640"),
            ("-79.42780803106380", "37.80076801128810"),
            ("-79.42790415883020", "37.80075971271620"),
            ("-79.42799954554300", "37.80080955449520"),
            ("-79.42804103733830", "37.80086964276790"),
            ("-79.42808088870150", "37.80093986171380"),
            ("-79.42806338028960", "37.80098181666410"),
            ("-79.42795981960920", "37.80104392146650"),
            ("-79.42787772215950", "37.80107981243970"),
            ("-79.42775354958400", "37.80113206730090"),
            ("-79.42768488982480", "37.80120559044890"),
            ("-79.42765420267700", "37.80131915378600"),
            ("-79.42763326178760", "37.8014863097879"),
            ("-79.42762414515990", "37.80158744329420"),
            ("-79.42762276901460", "37.80171154705220"),
            ("-79.42766204957610", "37.8018313617281"),
            ("-79.42774522148180", "37.80190332554240"),
            ("-79.42784372311350", "37.80193406868100"),
            ("-79.42796458078270", "37.80193793446630"),
            ("-79.42810137785380", "37.80193352589620"),
            ("-79.42830733982090", "37.80193732833920"),
            ("-79.42847498764080", "37.8019486564089"),
            ("-79.42860893012770", "37.80199380876300"),
            ("-79.42872915882780", "37.8020562725611"),
            ("-79.42872898820060", "37.80209420927230"),
            ("-79.42857123590750", "37.80227042306330"),
            ("-79.42832240444440", "37.8025445961007"),
            ("-79.4281958925536", "37.80267318118160"),
            ("-79.42807405689460", "37.80279803131730"),
            ("-79.42799355632550", "37.8028670527386"),
            ("-79.4280689055668", "37.80294148080750"),
            ("-79.42821407574910", "37.80302616798680"),
            ("-79.42845374855590", "37.80312768334240"),
            ("-79.42885400222770", "37.80331811934570"),
            ("-79.4299954201127", "37.80396217362600"),
            ("-79.43006450328490", "37.80399735015100"),
            ("-79.43014674262320", "37.80399137352570"),
            ("-79.43020636883220", "37.8039438407023"),
            ("-79.43024469950800", "37.80388655907210"),
            ("-79.43029030202470", "37.80378266698180"),
            ("-79.43038540658190", "37.80359191088490"),
            ("-79.43050840520760", "37.80343082222580"),
            ("-79.43067575418800", "37.80324919037120"),
            ("-79.43081627888610", "37.80312957336930"),
            ("-79.43097395799420", "37.8029726279921"),
            ("-79.43110435106240", "37.80284101674930"),
            ("-79.43119367660930", "37.8026968794032"),
            ("-79.43123008885550", "37.80254703138370"),
            ("-79.43120746231250", "37.80238606055800"),
            ("-79.43106056754960", "37.80226230550190"),
            ("-79.43085635430020", "37.80221964431540"),
            ("-79.43071717121330", "37.80221625411970"),
            ("-79.43061339604680", "37.8022326214062"),
            ("-79.43048461968030", "37.80227751899330"),
            ("-79.43037676159080", "37.8023144549094"),
            ("-79.43025575047350", "37.80238665151870"),
            ("-79.43011598722990", "37.80248834962100"),
            ("-79.43005234154880", "37.80260416756070"),
            ("-79.43004318075620", "37.80271032274860"),
            ("-79.43005882186310", "37.80282438350500"),
            ("-79.43009996455850", "37.80294110498260"),
            ("-79.43015802338370", "37.80307509467590"),
            ("-79.43019595248730", "37.80319374286100"),
            ("-79.43023598271390", "37.80335680587610"),
            ("-79.43025697331890", "37.80348154953010"),
            ("-79.43028571984530", "37.8036568077848"),
            ("-79.4302670911637", "37.80374624541830"),
            ("-79.43027098472070", "37.80382301035730"),
            ("-79.43022801659120", "37.80386909063560"),
            ("-79.43015901041320", "37.80395530315120"),
            ("-79.43010351397490", "37.80397676858640"),
            ("-79.43002907501120", "37.80395419337030"),
            ("-79.42989187923300", "37.80387911874030"),
            ("-79.42855519880180", "37.80315223875290"),
            ("-79.42814713425230", "37.8029805385992"),
            ("-79.42803186471000", "37.80287084462750"),
            ("-79.42795587411590", "37.80290781386560"),
            ("-79.42768300341370", "37.80318793190650"),
            ("-79.42749397503240", "37.80335768198040"),
            ("-79.42689843902310", "37.80385990583950"),
            ("-79.42643534401380", "37.80421714555640"),
            ("-79.42604139875950", "37.80451490328670"),
            ("-79.42594792791340", "37.80453767756620"),
            ("-79.4258269547428", "37.8045126835036"),
            ("-79.42572211530200", "37.80445580333820"),
            ("-79.42562777445070", "37.80439801372240"),
            ("-79.42465806725810", "37.80393159298910"),
            ("-79.42277544335500", "37.80298168530710"),
            ("-79.42101564095640", "37.80213028522090"),
            ("-79.42027546699380", "37.80164553198400"),
            ("-79.41939952159850", "37.80067490723480"),
            ("-79.41909093412600", "37.80034302147090"),
            ("-79.41882200967240", "37.80010907420800"),
            ("-79.41852547137360", "37.79984994937390"),
            ("-79.41819723920260", "37.79952343392400"),
            ("-79.41812937473260", "37.79945719796650"),
            ("-79.41968256044460", "37.79873213797030"),
            ("-79.42055006901730", "37.79821539596380"),
            ("-79.42090547274960", "37.79797507074870"),
            ("-79.42112036404030", "37.7978050506827"),
            ("-79.4214296618308", "37.79758077375300"),
            ("-79.42230434875390", "37.79680257102270"),
            ("-79.42270234789680", "37.7963529974059"),
            ("-79.42389524604820", "37.79488042155010"),
            ("-79.42435023213950", "37.79438511310470"),
            ("-79.42487289519320", "37.79386410237630"),
            ("-79.42528804251890", "37.79351809096410"),
            ("-79.42572201932670", "37.79317393109810"),
            ("-79.42590362753740", "37.79299793295420"),
            ("-79.42762502070860", "37.79171344318300"),
            ("-79.42926861468700", "37.79031648044450"),
            ("-79.42997144730150", "37.78971205273150"),
            ("-79.43032439691900", "37.78952230299750"),
            ("-79.43067408982950", "37.78947184584450"),
            ("-79.43106120766100", "37.78946333122600"),
            ("-79.4313732661623", "37.78950336392650"),
            ("-79.43165087471060", "37.78955522497080"),
            ("-79.43199748142890", "37.78959201748130"),
            ("-79.43253090868070", "37.78963347501770"),
            ("-79.43279457604950", "37.78968105769560"),
            ("-79.43332073708610", "37.78969361829440"),
            ("-79.43371581236490", "37.78967954768410"),
            ("-79.43413822285850", "37.78965460097660"),
            ("-79.43463195447250", "37.78959659627370"),
            ("-79.43497596442430", "37.78956653426150"),
            ("-79.435271533773", "37.78947543879700"),
            ("-79.43561980910690", "37.78936127166010"),
            ("-79.43588534471430", "37.78929181649990"),
            ("-79.43617972971950", "37.78919658355150"),
            ("-79.43737995265430", "37.78871886125230"),
            ("-79.43844378182560", "37.7883554011194"),
            ("-79.43896954479130", "37.78816016014060"),
            ("-79.43912878040380", "37.788107641795"),
            ("-79.44006958933680", "37.78754589218290"),
            ("-79.44028642534630", "37.78734456821560"),
            ("-79.4404775816363", "37.78716712011020"),
            ("-79.44056584651820", "37.78713578335830"),
            ("-79.44070368265880", "37.78710051090140"),
            ("-79.44084119754680", "37.78706526751370"),
            ("-79.44096407528240", "37.78704285032230"),
            ("-79.44111894782130", "37.78699283365440"),
            ("-79.44122400500240", "37.78694709960690"),
            ("-79.44134112217160", "37.78686462019410"),
            ("-79.44147577762980", "37.78674651213250"),
            ("-79.44159500906560", "37.78664613415010"),
            ("-79.44167225910770", "37.78657921671290"),
            ("-79.4427402449891", "37.78561281124540"),
            ("-79.44349044466000", "37.78615123297480"),
            ("-79.44422473529990", "37.78672054132040"),
            ("-79.4446039037487", "37.78697523876900")]

blueRoute = [("-79.44454884712100", "37.78694311560170"),
             ("-79.44506262989720", "37.78729093558580"),
             ("-79.44529679148860", "37.78737825485410"),
             ("-79.44552715452200", "37.78736165758190"),
             ("-79.44593572197760", "37.78724133327550"),
             ("-79.44630385483010", "37.78712814206270"),
             ("-79.44651422554410", "37.78705428183490"),
             ("-79.44670058934820", "37.78693275243600"),
             ("-79.44751052997280", "37.78752274529890"),
             ("-79.44812562069300", "37.7879818909857"),
             ("-79.44911365016940", "37.78872250774800"),
             ("-79.44873425932890", "37.78896972063840"),
             ("-79.44862087297220", "37.78893939346420"),
             ("-79.44831019441720", "37.78886016128770"),
             ("-79.44793456658570", "37.7887067144291"),
             ("-79.44759388770620", "37.78862330178640"),
             ("-79.44742216522780", "37.78869044418530"),
             ("-79.44715916106710", "37.78888340772560"),
             ("-79.44699924100820", "37.78907619050770"),
             ("-79.4467118883218", "37.78928571510220"),
             ("-79.44653593833690", "37.7894351987632"),
             ("-79.44646569609070", "37.78963749318100"),
             ("-79.44652266021730", "37.78985712500790"),
             ("-79.44662704705110", "37.78992658327490"),
             ("-79.44683132427350", "37.78993603986320"),
             ("-79.44705063361150", "37.78989120227390"),
             ("-79.4472522817819", "37.78981892514050"),
             ("-79.44753991194680", "37.78960812381730"),
             ("-79.44769962653880", "37.78938325831160"),
             ("-79.44783907029630", "37.78914933720270"),
             ("-79.44792420875690", "37.78902322739970"),
             ("-79.44808771978430", "37.7889300084386"),
             ("-79.44823462749420", "37.78889223810590"),
             ("-79.44836200492620", "37.7888880453678"),
             ("-79.44847630785670", "37.78891341497680"),
             ("-79.448661272164", "37.78896411182930"),
             ("-79.44877371751140", "37.78895336050200"),
             ("-79.44885103224050", "37.78889658994670"),
             ("-79.44904813122360", "37.78876828799980"),
             ("-79.4491181325419", "37.78873804903970"),
             ("-79.45054765314080", "37.78980298721970"),
             ("-79.45236996350410", "37.79112637999510"),
             ("-79.45410701698440", "37.79241521701720"),
             ("-79.45485131809480", "37.79320211474870"),
             ("-79.45578204652980", "37.79444435945100"),
             ("-79.45667739773410", "37.79568347123930"),
             ("-79.4573605171057", "37.7965790587123"),
             ("-79.45826290479270", "37.79770172988220"),
             ("-79.4589739604293", "37.79835778811090"),
             ("-79.45965457802290", "37.79883962546200"),
             ("-79.46090107932760", "37.79964782391460"),
             ("-79.46058796061040", "37.79994928669290"),
             ("-79.46017861826440", "37.80034564499000"),
             ("-79.45990874245070", "37.80054884428000"),
             ("-79.45981538023410", "37.80056824050290"),
             ("-79.45967657747530", "37.80057358849640"),
             ("-79.45918142694150", "37.800482098185"),
             ("-79.45957681862600", "37.80057894702810"),
             ("-79.45978729781980", "37.80060359425310"),
             ("-79.45999042121360", "37.8005186482072"),
             ("-79.46028655722500", "37.80027646068950"),
             ("-79.46051310645140", "37.80003756891970"),
             ("-79.46073561023440", "37.79981644808850"),
             ("-79.46093057451800", "37.7996362804319"),
             ("-79.45955778120400", "37.79875928483350"),
             ("-79.45883869975970", "37.79822760129250"),
             ("-79.45857283244930", "37.79798669236030"),
             ("-79.45808329583820", "37.7974929172898"),
             ("-79.45775923300800", "37.79711666964620"),
             ("-79.45696026494270", "37.79608024653890"),
             ("-79.45633250003120", "37.79518341917240"),
             ("-79.45566867826910", "37.79425539649300"),
             ("-79.45494724276670", "37.79328971248900"),
             ("-79.45459954684930", "37.79289332722580"),
             ("-79.45403091068170", "37.79231568020620"),
             ("-79.45330518681430", "37.79178354502870"),
             ("-79.45244743895170", "37.7911423089217"),
             ("-79.45230895386850", "37.79125239510640"),
             ("-79.45222620666430", "37.79138254041600"),
             ("-79.45216084609920", "37.79150929400250"),
             ("-79.45199022240470", "37.7916671926333"),
             ("-79.45157465891670", "37.79199713037340"),
             ("-79.45126578335030", "37.79222499200290"),
             ("-79.45100473990460", "37.79236681780450"),
             ("-79.4507440877432", "37.79244916444260"),
             ("-79.45029130834940", "37.79256921427310"),
             ("-79.44999169225720", "37.7926463277356"),
             ("-79.4498246110257", "37.7927779755658"),
             ("-79.44971836303420", "37.79303054691560"),
             ("-79.44935840051240", "37.79362526189830"),
             ("-79.4488469919628", "37.79426262278380"),
             ("-79.44869472429240", "37.79437760980120"),
             ("-79.44834326102890", "37.79443083500500"),
             ("-79.44803707725270", "37.7944515907916"),
             ("-79.44778875418830", "37.79440564299270"),
             ("-79.44761754759570", "37.7943608648737"),
             ("-79.44723914255150", "37.79414069798970"),
             ("-79.44703657936410", "37.79398241713850"),
             ("-79.44676892529400", "37.79363037711830"),
             ("-79.44644261077280", "37.79330979183760"),
             ("-79.44597583728230", "37.79310822303880"),
             ("-79.44477187330150", "37.79261040269540"),
             ("-79.44448221423820", "37.79249951975360"),
             ("-79.44428433945280", "37.79246317097840"),
             ("-79.44371019398330", "37.79212716823750"),
             ("-79.44355017263420", "37.79204666642750"),
             ("-79.44333408995850", "37.79207215377150"),
             ("-79.44306545772970", "37.79207361769180"),
             ("-79.44294746499700", "37.79202294295870"),
             ("-79.44287913638740", "37.79189367822640"),
             ("-79.44289069263420", "37.79176225104540"),
             ("-79.4435854506807", "37.79099057128460"),
             ("-79.44405797984070", "37.79046738335110"),
             ("-79.44450310531000", "37.79000884720500"),
             ("-79.44506984846590", "37.78945302044160"),
             ("-79.44532995088160", "37.78919278370720"),
             ("-79.44579822729070", "37.78869947528150"),
             ("-79.44594702424090", "37.78860929913090"),
             ("-79.44613128759190", "37.78858026118380"),
             ("-79.44641718272220", "37.78857462179950"),
             ("-79.44656462616350", "37.78855450048680"),
             ("-79.44680478920930", "37.78831643262440"),
             ("-79.44734703075530", "37.78771355673150"),
             ("-79.44748224067400", "37.78753971905910"),
             ("-79.44745552827860", "37.78749664222830"),
             ("-79.446719408576", "37.78694573219000"),
             ("-79.44647358089170", "37.78709348628710"),
             ("-79.44612487631010", "37.78718271607690"),
             ("-79.44570911959270", "37.78730787675750"),
             ("-79.44542328926190", "37.78738068074800"),
             ("-79.44525119323810", "37.78737807436950"),
             ("-79.44512324903450", "37.78732795697610"),
             ("-79.44460279173750", "37.7869949094738"),
             ("-79.44348351195640", "37.7861459914139"),
             ("-79.44274255867610", "37.78561887250200"),
             ("-79.44451425106990", "37.78403321495280"),
             ("-79.44540640873130", "37.78322940563880"),
             ("-79.44608428798120", "37.78264252989820"),
             ("-79.44668349509510", "37.78210309715860"),
             ("-79.44736274205590", "37.78147635584620"),
             ("-79.44660783703650", "37.78095347401300"),
             ("-79.44633561605260", "37.78120433215450"),
             ("-79.44601664229000", "37.78146283222190"),
             ("-79.44567905233360", "37.78176126727430"),
             ("-79.44538855561610", "37.78202308635690"),
             ("-79.44438962905290", "37.7828969268808"),
             ("-79.4429763568963", "37.78415937080690"),
             ("-79.4419526920896", "37.78345992905220"),
             ("-79.44154753962550", "37.78318710574670"),
             ("-79.44108669491230", "37.78283447410530"),
             ("-79.44052512754250", "37.78242721493540"),
             ("-79.43969707737130", "37.78186133840660"),
             ("-79.43847013397520", "37.78285821311530"),
             ("-79.44002893885090", "37.78387922900120"),
             ("-79.44048035309590", "37.78409358684010"),
             ("-79.44119202707690", "37.78449296191470"),
             ("-79.4419676589671", "37.78504633519670"),
             ("-79.44096798095450", "37.78593913036080"),
             ("-79.4408383721164", "37.78610449817450"),
             ("-79.44062627658250", "37.78647921425810"),
             ("-79.44050929566470", "37.7869314293502"),
             ("-79.44053982779700", "37.78699785425820"),
             ("-79.44058573621720", "37.78704197689560"),
             ("-79.44065132008320", "37.78706037912090"),
             ("-79.44073939527670", "37.78706322905490"),
             ("-79.44093069937340", "37.78704672248590"),
             ("-79.44107000469110", "37.78700296809930"),
             ("-79.44117502832430", "37.78696355671240"),
             ("-79.44144886200450", "37.78674901836470"),
             ("-79.4427282206105", "37.78562837640250"),
             ("-79.44349055211410", "37.78616954002530"),
             ("-79.44430759954940", "37.78677531318660"),
             ("-79.44454884712100", "37.78694311560170")]

busNumber = 1
whichRoute = redRoute

def main():
    pointClient.init()
    idx = randint(0, len(whichRoute)-1)
    while True:
        (longGPS, latGPS) = whichRoute[idx]
        pointClient.request("POST Traveller Bus #" + str(busNumber) + " " + longGPS + " " + latGPS)
        if idx+1 >= len(whichRoute):
            idx = 0
        else:
            idx += 1
        sleep(1)

if __name__ == "__main__":
    main()

