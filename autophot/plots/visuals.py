import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib
import os

__all__ = ["main_pallet", "cmap_grad", "cmap_div"]

main_pallet = {
    "primary1": "#5FAD41",
    "primary2": "#46A057",
    "primary3": "#2D936C",
    "secondary1": "#595122",
    "secondary2": "#BFAE48",
    "pop": "#391463",
}

# grad_list = [
#     "#000000",
#     "#1A1F16",
#     "#1E3F20",
#     "#335E31",  # "#294C28",
#     "#477641",  # "#345830",
#     "#5D986D",  # "#4A7856",
#     "#88BF9E",  # "#6FB28A",
#     "#94ECBE",
#     "#FFFFFF",
# ]

# grad_list = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rgb_colours.npy"))
# not proud of this but it works
grad_list = [
    [0.02352941176470601, 0.05490196078431372, 0.03137254901960787],
    [0.025423221664412132, 0.057920953380312966, 0.033516620406216086],
    [0.027376785284830882, 0.06093685701603565, 0.035720426678078974],
    [0.02938891743876659, 0.0639504745699993, 0.03798295006291389],
    [0.03145841869575705, 0.06696255038243151, 0.04030317185736432],
    [0.033584075048444885, 0.06997377604547542, 0.04260833195845542],
    [0.03576465765226276, 0.07298479546414544, 0.044888919486002675],
    [0.03799892263356237, 0.0759962092973116, 0.0471477168479796],
    [0.04028561096212802, 0.07900857886908796, 0.049385189300118405],
    [0.04255435348091496, 0.08202242962578685, 0.05160177112762838],
    [0.04479522750797262, 0.0850382542012795, 0.053797868796876404],
    [0.047011290960205, 0.08805651514356005, 0.05597386374386699],
    [0.04920301153517722, 0.09107764734708199, 0.05813011485045571],
    [0.05137081101697757, 0.09410206022865564, 0.06026696065107289],
    [0.05351507020340438, 0.09713013967907827, 0.062384721306060466],
    [0.05563613318418619, 0.1001622498180042, 0.06448370037222773],
    [0.057734311075703586, 0.10319873457564618, 0.06656418639667772],
    [0.0598098852979892, 0.10623991912163352, 0.0686264543561699],
    [0.06186311046428467, 0.10928611115857814, 0.07067076696111699],
    [0.06389421694104419, 0.11233760209556845, 0.07269737584065203],
    [0.06590341312637987, 0.11539466811482368, 0.07470652262295904],
    [0.06789088748697142, 0.11845757114304345, 0.07669843992315992],
    [0.06985681038697011, 0.12152655973754478, 0.07867335224943414],
    [0.07180133573715267, 0.12460186989603428, 0.08063147683667268],
    [0.07372460248826435, 0.12768372579779083, 0.08257302441578668],
    [0.07562673598889558, 0.13077234048311664, 0.08449819992578214],
    [0.07750784922530482, 0.1338679164771084, 0.0864072031748393],
    [0.0793680439581338, 0.13697064636311304, 0.08830022945588598],
    [0.08120741176889373, 0.14008071331062474, 0.0901774701215026],
    [0.08302603502740363, 0.1431982915618533, 0.09203911312243368],
    [0.08482398778987404, 0.14632354688073884, 0.0938853435134896],
    [0.08660133663613406, 0.14945663696777384, 0.09571634393019346],
    [0.08835814145343088, 0.15259771184365092, 0.0975322950391592],
    [0.09009445617335096, 0.15574691420443426, 0.09933337596485287],
    [0.09181032946766504, 0.1589043797506794, 0.10111976469511005],
    [0.09350580540821188, 0.16207023749268656, 0.1028916384675223],
    [0.0951809240954313, 0.16524461003384922, 0.1046491741385914],
    [0.09683572225960263, 0.1684276138338816, 0.10639254853734492],
    [0.09847023383851092, 0.17161935945352033, 0.10812193880494256],
    [0.10008449053481877, 0.17481995178216395, 0.10983752272163866],
    [0.10167852235616967, 0.1780294902497653, 0.11153947902233724],
    [0.10325235814074307, 0.18124806902417712, 0.11322798770185102],
    [0.10480602607076109, 0.18447577719504085, 0.1149032303108651],
    [0.10633955417621349, 0.18771269894521686, 0.11656539024350993],
    [0.10785297083092218, 0.19095891371065837, 0.11821465301736292],
    [0.10934630524287259, 0.19421449632956456, 0.11985120654661363],
    [0.11081958794061691, 0.19747951718156898, 0.12147524140906224],
    [0.11227285125743197, 0.20075404231766003, 0.12308695110755152],
    [0.113706129814793, 0.2040381335814737, 0.12468653232637883],
    [0.11511946100664691, 0.20733184872254534, 0.12627418518317554],
    [0.1165128854858628, 0.21063524150205992, 0.12785011347669853],
    [0.11788644765418299, 0.21394836179160054, 0.12941452493092973],
    [0.11924019615691589, 0.21727125566535316, 0.13096763143583748],
    [0.12057418438355699, 0.2206039654861931, 0.13250964928512182],
    [0.12188847097547184, 0.2239465299860438, 0.13404079941121932],
    [0.12318312034172044, 0.2272989843408748, 0.13556130761782226],
    [0.12445820318406359, 0.23066136024067158, 0.13707140481012495],
    [0.12571379703214872, 0.2340336859546926, 0.13857132722298834],
    [0.12694998678982505, 0.23741598639230338, 0.14006131664718174],
    [0.1281668652935146, 0.2408082831596569, 0.14154162065383566],
    [0.12936453388351488, 0.24421059461247346, 0.14301249281721415],
    [0.13054310298908373, 0.24762293590515277, 0.14447419293589053],
    [0.13170269272811447, 0.25104531903643956, 0.1459269872523864],
    [0.1328434335221802, 0.25447775289184116, 0.14737114867131162],
    [0.1339654667276644, 0.2579202432829991, 0.14880695697601956],
    [0.13506894528368824, 0.26137279298418187, 0.15023469904377038],
    [0.1361540343774794, 0.26483540176607334, 0.15165466905937425],
    [0.13722091212776352, 0.2683080664270149, 0.15306716872726295],
    [0.1382697702867517, 0.271790780821844, 0.15447250748191957],
    [0.13930081496119553, 0.2752835358884738, 0.1558710026965733],
    [0.14031426735293703, 0.2787863196723416, 0.15726297989004664],
    [0.1413103645193169, 0.2822991173488483, 0.15864877293161908],
    [0.142289360153694, 0.28582191124391093, 0.16002872424375406],
    [0.1432515253862969, 0.2893546808527299, 0.16140318500251255],
    [0.1441971496054517, 0.29289740285688415, 0.16277251533545473],
    [0.14512654129921948, 0.29645005113984313, 0.16413708451681472],
    [0.1460400289172567, 0.3000125968009987, 0.1654972711597065],
    [0.14693796175266738, 0.30358500816829653, 0.16685346340510454],
    [0.14782071084339368, 0.3071672508095593, 0.16820605910731407],
    [0.14868866989260401, 0.31075928754257476, 0.16955546601563484],
    [0.14954225620729, 0.3143610784440312, 0.1709021019518895],
    [0.1503819116541449, 0.31797258085736924, 0.1722463949834796],
    [0.15120810363154275, 0.32159374939962293, 0.17358878359160151],
    [0.1520213260562527, 0.32522453596731304, 0.17492971683424066],
    [0.15282210036320543, 0.32886488974146083, 0.1762696545035385],
    [0.15361097651642713, 0.33251475719178275, 0.17760906727710982],
    [0.15438853402891373, 0.3361740820801234, 0.17894843686287198],
    [0.15515538298892081, 0.3398428054631865, 0.18028825613691796],
    [0.15591216508980174, 0.34352086569461787, 0.18162902927396304],
    [0.15665955466015927, 0.3472081984264961, 0.18297127186986703],
    [0.15739825969072788, 0.3509047366102775, 0.1843155110557227],
    [0.1581290228539065, 0.35461041049725495, 0.18566228560298584],
    [0.15885262251157475, 0.35832514763856854, 0.18701214601910962],
    [0.1595698737062211, 0.36204887288482673, 0.1883656546331343],
    [0.16028162913006866, 0.365781508385379, 0.18972338567067223],
    [0.1609887800663473, 0.3695229735872851, 0.19108592531772042],
    [0.1616922572963582, 0.3732731852340314, 0.19245387177272855],
    [0.1623930319654953, 0.3770320573640352, 0.19382783528634243],
    [0.1630921164008896, 0.38079950130898077, 0.1952084381882439],
    [0.16379056487278745, 0.38457542569203246, 0.19659631490050877],
    [0.16448947429132857, 0.38835973642596816, 0.19799211193690508],
    [0.16518998482987113, 0.39215233671127353, 0.19939648788756642],
    [0.1658932804655635, 0.3959531270342421, 0.20081011338847304],
    [0.166600589427405, 0.39976200516512433, 0.20223367107520046],
    [0.16731318454171665, 0.4035788661563645, 0.20366785552039823],
    [0.1680323834645103, 0.4074036023409737, 0.20511337315448636],
    [0.16875954879008526, 0.4112361033310768, 0.20657094216908256],
    [0.16949608802490335, 0.4150762560166792, 0.20804129240268987],
    [0.17024345341575386, 0.4189239445646968, 0.20952516520821696],
    [0.17100314162122876, 0.42277905041829333, 0.21102331330192792],
    [0.17177669321562006, 0.4266414522965662, 0.21253650059345497],
    [0.1725656920146934, 0.43051102619463094, 0.21406550199656194],
    [0.17337176421315095, 0.43438764538414765, 0.2156111032203738],
    [0.174196577324217, 0.4382711804143329, 0.21717410054084768],
    [0.1750418389125363, 0.4421614991135102, 0.21875530055231346],
    [0.1759092951125111, 0.44605846659124265, 0.22035551989895852],
    [0.17680072892538157, 0.4499619452410963, 0.22197558498620257],
    [0.17771795828963766, 0.4538717947440886, 0.2236163316719602],
    [0.178662833920936, 0.45778787207287114, 0.22527860493786028],
    [0.1796372369194738, 0.46171003149669404, 0.22696325854055394],
    [0.18064307614457878, 0.46563812458721304, 0.22867115464331578],
    [0.18168228535855538, 0.4695720002251926, 0.23040316342821293],
    [0.1827568201439772, 0.47351150460815455, 0.23216016268918455],
    [0.1838686546011176, 0.477456481259039, 0.233943037406457],
    [0.18501977783468404, 0.48140677103593116, 0.23575267930278093],
    [0.18621219024170063, 0.4853622121429166, 0.23758998638206003],
    [0.18744789961499414, 0.4893226401421262, 0.23945586245100942],
    [0.1887289170794073, 0.49328788796703654, 0.24135121662454895],
    [0.19005725288048025, 0.4972577859370923, 0.24327696281571337],
    [0.19143491204781923, 0.5012321617737128, 0.24523401921092142],
    [0.19286388995773657, 0.505210840617762, 0.2472233077315104],
    [0.1943461678218979, 0.509193645048545, 0.24924575348250605],
    [0.1958837081305836, 0.5131803951044065, 0.2513022841896479],
    [0.1974784500806806, 0.5171709083050143, 0.25339382962574203],
    [0.1991323050198725, 0.5211649996753929, 0.2555213210274589],
    [0.20084715193916947, 0.5251624817718009, 0.2576856905037352],
    [0.20262483304633028, 0.5291631647095255, 0.2598878704369637],
    [0.204467149452764, 0.5331668561926818, 0.26212879287818813],
    [0.206375857005755, 0.5371733615461064, 0.2644093889375338],
    [0.20835266229704946, 0.5411824837494301, 0.26673058817112216],
    [0.2103992188771397, 0.5451940234734288, 0.26909331796570707],
    [0.21251712370282538, 0.5492077791187413, 0.2714985029222856],
    [0.21470791384316384, 0.5532235468570559, 0.2739470642399031],
    [0.21697306346622774, 0.5572411206748591, 0.27643991910086557],
    [0.21931398112597572, 0.5612602924198622, 0.2789779800585389],
    [0.22173200736531357, 0.5652808518501962, 0.28156215442887567],
    [0.22422841264772203, 0.5693025866864954, 0.28419334368676863],
    [0.2268043956263523, 0.5733252826669735, 0.2868724428682829],
    [0.22946108175552465, 0.5773487236056106, 0.28960033997974594],
    [0.23219952224604845, 0.5813726914535655, 0.2923779154146281],
    [0.23502069336196157, 0.5853969663639336, 0.29520604137906364],
    [0.23792549605282798, 0.5894213267599773, 0.2980855813267848],
    [0.24091475591248918, 0.5934455494069475, 0.30101738940417244],
    [0.2439892234519782, 0.5974694094876285, 0.3040023099060248],
    [0.2471495746716238, 0.6014926806817401, 0.3070411767425731],
    [0.2503964119149868, 0.6055151352493269, 0.31013481291816875],
    [0.25373026498509416, 0.6095365441182762, 0.3132840300219835],
    [0.25715159250188796, 0.6135566769761028, 0.3164896277309624],
    [0.26066078347841287, 0.6175753023661407, 0.31975239332517896],
    [0.26425815909238537, 0.6215921877882963, 0.3230731012156454],
    [0.26794397462927927, 0.6256070998045035, 0.32645251248454027],
    [0.27171842157278525, 0.6296198041490337, 0.32989137443772115],
    [0.2755816298187335, 0.6336300658438219, 0.3333904201693042],
    [0.27953366998896156, 0.6376376493189533, 0.3369503681380034],
    [0.2835745558223273, 0.6416423185384807, 0.34057192175484835],
    [0.2877042466209889, 0.6456438371317278, 0.3442557689818123],
    [0.2919226497312409, 0.6496419685302498, 0.34800258194081274],
    [0.2962296230395252, 0.6536364761106029, 0.3518130165324921],
    [0.30062497746549316, 0.6576271233431101, 0.3556877120641009],
    [0.3051084794357496, 0.6616136739467778, 0.3596272908857725],
    [0.3096798533232689, 0.6655958920505426, 0.3636323580344192],
    [0.3143387838391119, 0.6695735423610237, 0.3677035008844355],
    [0.3190849183647877, 0.6735463903369483, 0.37184128880436657],
    [0.3239178692149385, 0.677514202370436, 0.37604627281865705],
    [0.3288372158217989, 0.6814767459753105, 0.38031898527358976],
    [0.33384250683409117, 0.6854337899826277, 0.3846599395064855],
    [0.33893326212463143, 0.68938510474359, 0.38906962951724855],
    [0.344108974702066, 0.6933304623400306, 0.39354852964131404],
    [0.34936911252340047, 0.697269636802651, 0.398097094223074],
    [0.354713120205116, 0.7012024043371861, 0.40271575728885467],
    [0.3601404206316701, 0.7051285435586824, 0.407404932218529],
    [0.365650416461051, 0.7090478357340677, 0.4121650114148717],
    [0.3712424915278934, 0.7129600650331871, 0.4169963659697734],
    [0.3769160121453231, 0.7168650187884974, 0.4218993453264664],
    [0.3826703283074528, 0.7207624877635708, 0.426874276936929],
    [0.38850477479467865, 0.724652266430624, 0.4319214659136745],
    [0.39441867218475135, 0.7285341532572063, 0.4370411946751511],
    [0.4004113277726398, 0.7324079510022498, 0.4422337225840276],
    [0.40648203640264285, 0.7362734670216392, 0.4474992855776477],
    [0.41263008121642264, 0.7401305135834749, 0.4528380957899934],
    [0.41885473432075093, 0.7439789081931996, 0.4582503411645124],
    [0.42515525737890464, 0.74781847392875, 0.4637361850571962],
    [0.4315309021296915, 0.7516490397859019, 0.4692957658293329],
    [0.4379809108381271, 0.755470441033972, 0.4749291964293609],
    [0.44450451668174257, 0.7592825195820302, 0.4806365639632952],
    [0.4511009440764859, 0.7630851243557921, 0.48641792925318267],
    [0.4577694089460426, 0.766878111685348, 0.49227332638307436],
    [0.46450911893842234, 0.7706613457038759, 0.49820276223198207],
    [0.47131927359337594, 0.7744346987575222, 0.5042062159932884],
    [0.47819906446422616, 0.7781980518265826, 0.5102836386800519],
    [0.4851476751974689, 0.7819512949581628, 0.5164349526156181],
    [0.4921642815733072, 0.7856943277104902, 0.5226600509088999],
    [0.49924805151023793, 0.7894270596090324, 0.528958796913626],
    [0.506398145036514, 0.7931494106146145, 0.5353310236707783],
    [0.5136137142311699, 0.7968613116037284, 0.5417765333333355],
    [0.5208939031371336, 0.8005627048612254, 0.5482950965723069],
    [0.528237847648764, 0.8042535445856207, 0.5548864519629064],
    [0.5356446753758648, 0.8079337974072546, 0.5615503053495099],
    [0.5431135054862372, 0.8116034429195591, 0.5682863291878316],
    [0.5506434485283842, 0.8152624742237489, 0.5750941618624987],
    [0.558233606235997, 0.8189108984872628, 0.5819734069778754],
    [0.5658830713155681, 0.8225487375163245, 0.588923632619649],
    [0.5735909272182081, 0.8261760283430954, 0.5959443705842361],
    [0.5813562478966682, 0.8297928238278868, 0.6030351155725882],
    [0.5891780975482949, 0.8333991932770318, 0.6101953243443609],
    [0.5970555303443447, 0.8369952230771135, 0.6174244148277456],
    [0.6049875901460008, 0.8405810173463196, 0.6247217651794131],
    [0.6129733102071075, 0.8441566986038703, 0.6320867127880987],
    [0.6210117128633796, 0.8477224084586106, 0.6395185532141892],
    [0.629101809207598, 0.8512783083180583, 0.6470165390563735],
    [0.6372425987500262, 0.8548245801194263, 0.6545798787348152],
    [0.6454330690629193, 0.8583614270844092, 0.6622077351784434],
    [0.6536721954076695, 0.861889074499868, 0.6698992244017301],
    [0.6619589403427637, 0.8654077705269353, 0.6776534139536473],
    [0.670292253310307, 0.868917787041518, 0.6854693212183214],
    [0.6786710701982759, 0.8724194205097873, 0.6933459115430326],
    [0.6870943128752733, 0.8759129929029018, 0.7012820961645896],
    [0.6955608886937588, 0.8793988526560546, 0.7092767298994272],
    [0.7040696899570745, 0.8828773756779759, 0.7173286085559195],
    [0.7126195933446154, 0.8863489664182553, 0.7254364660189113],
    [0.7212094592884835, 0.8898140590014009, 0.7335989709460631],
    [0.7298381312936156, 0.8932731184384776, 0.7418147230026438],
    [0.738504435191736, 0.8967266419295534, 0.7500822485452499],
    [0.7472071783175026, 0.900175160273203, 0.7583999956446169],
    [0.755945148592551, 0.9036192394031619, 0.7667663283120103],
    [0.7647171134997374, 0.9070594820771404, 0.7751795197609306],
    [0.7735218189254033, 0.9104965297491636, 0.783637744493875],
    [0.7823579878412776, 0.9139310646651907, 0.7921390689495337],
    [0.79122431878925, 0.9173638122327802, 0.8006814403748957],
    [0.8001194841201199, 0.9207955437304958, 0.8092626734934449],
    [0.8090421279203749, 0.9242270794429251, 0.817880434416763],
    [0.8179908635354565, 0.9276592923352225, 0.8265322210808196],
    [0.8269642705600306, 0.9310931124203533, 0.8352153392634705],
    [0.8359608911072839, 0.934529532028408, 0.8439268729323351],
    [0.844979225077973, 0.9379696122690698, 0.852663647247446],
    [0.8540177240040997, 0.9414144910996233, 0.8614221819497985],
    [0.863074782804233, 0.9448653935946189, 0.8701986320294973],
    [0.8721487283913724, 0.9483236452977989, 0.87898871137326],
    [0.8812378033992858, 0.9517906899876957, 0.8877875933734316],
    [0.890340142117086, 0.955268113920236, 0.8965897799935405],
    [0.8994537336219597, 0.9587576798305327, 0.9053889271758421],
    [0.908576363256908, 0.9622613760595616, 0.9141776092709066],
    [0.9177055163843063, 0.9657814898283584, 0.9229469978386258],
    [0.9268382144426769, 0.9693207202671751, 0.9316864204851563],
    [0.9359707258804478, 0.9728823589346071, 0.9403827547526942],
    [0.9450980392156855, 0.9764705882352952, 0.9490196078431373],
]

cmap_grad = LinearSegmentedColormap.from_list("cmap_grad", grad_list)

# # grad_list = ["#000000", "#1A1F16", "#1E3F20", "#294C28", "#345830", "#4A7856", "#6FB28A", "#94ECBE", "#FFFFFF"]
# grad_cdict = {"red": [], "green": [], "blue": []}
# cpoints = np.linspace(0, 1, len(grad_list))
# for i in range(len(grad_list)):
#     grad_cdict["red"].append(
#         [cpoints[i], int(grad_list[i][1:3], 16) / 256, int(grad_list[i][1:3], 16) / 256]
#     )
#     grad_cdict["green"].append(
#         [cpoints[i], int(grad_list[i][3:5], 16) / 256, int(grad_list[i][3:5], 16) / 256]
#     )
#     grad_cdict["blue"].append(
#         [cpoints[i], int(grad_list[i][5:7], 16) / 256, int(grad_list[i][5:7], 16) / 256]
#     )
# cmap_grad = LinearSegmentedColormap("cmap_grad", grad_cdict)

div_list = [
    "#332A1F",
    "#514129",
    "#7C6527",
    "#A2862A",
    "#DAB944",
    "#FFFFFF",
    "#7EC87E",
    "#3EA343",
    "#267D2F",
    "#0D5D09",
    "#073805",
]
# div_list = ["#083D77", "#7E886B", "#B9AE65", "#FFFFFF", "#F1B555", "#EE964B", "#F95738"]
div_cdict = {"red": [], "green": [], "blue": []}
cpoints = np.linspace(0, 1, len(div_list))
for i in range(len(div_list)):
    div_cdict["red"].append(
        [cpoints[i], int(div_list[i][1:3], 16) / 256, int(div_list[i][1:3], 16) / 256]
    )
    div_cdict["green"].append(
        [cpoints[i], int(div_list[i][3:5], 16) / 256, int(div_list[i][3:5], 16) / 256]
    )
    div_cdict["blue"].append(
        [cpoints[i], int(div_list[i][5:7], 16) / 256, int(div_list[i][5:7], 16) / 256]
    )
cmap_div = LinearSegmentedColormap("cmap_div", div_cdict)

# P = plt.cm.plasma_r
# C = plt.cm.cividis
# N = 3
# cmap_div = ListedColormap(["#083D77", "#7E886B", "#B9AE65", "#FFFFFF", "#F1B555", "#EE964B", "#F95738"])

# main_pallet = {
#     "primary1": "g",
#     "primary2": "r",
#     "primary3": "b",
#     "primary4": "ornnge",
#     "primary5": "cyan",
#     "secondary1": "purple",
#     "secondary2": "salmon",
#     "secondary3": "k",
#     "pop": "yellow",
# }

# cmap_grad = plt.cm.magma
# cmap_div = plt.cm.seismic

# from matplotlib.colors import LinearSegmentedColormap
# cmaplist = ["#000000", "#720026", "#A0213F", "#ce4257", "#E76154", "#ff9b54", "#ffd1b1"]
# cdict = {"red": [], "green": [], "blue": []}
# cpoints = np.linspace(0, 1, len(cmaplist))
# for i in range(len(cmaplist)):
#     cdict["red"].append(
#         [cpoints[i], int(cmaplist[i][1:3], 16) / 256, int(cmaplist[i][1:3], 16) / 256]
#     )
#     cdict["green"].append(
#         [cpoints[i], int(cmaplist[i][3:5], 16) / 256, int(cmaplist[i][3:5], 16) / 256]
#     )
#     cdict["blue"].append(
#         [cpoints[i], int(cmaplist[i][5:7], 16) / 256, int(cmaplist[i][5:7], 16) / 256]
#     )
# autocmap = LinearSegmentedColormap("autocmap", cdict)
# autocolours = {
#     "red1": "#c33248",
#     "blue1": "#84DCCF",
#     "blue2": "#6F8AB7",
#     "redrange": ["#720026", "#A0213F", "#ce4257", "#E76154", "#ff9b54", "#ffd1b1"],
# }  # '#D95D39'
