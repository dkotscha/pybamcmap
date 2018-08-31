from matplotlib import colors, cm as mpl_cm

_bam_viridis_lut = [
   [ 0.00000000, 0.15686275, 0.19607843 ],
   [ 0.00000000, 0.15923106, 0.19924644 ],
   [ 0.00000000, 0.16159938, 0.20241446 ],
   [ 0.00000000, 0.16396770, 0.20558247 ],
   [ 0.00000000, 0.16633602, 0.20875048 ],
   [ 0.00000000, 0.16870434, 0.21191849 ],
   [ 0.00000000, 0.17107266, 0.21508651 ],
   [ 0.00000000, 0.17344098, 0.21825452 ],
   [ 0.00000000, 0.17580930, 0.22142253 ],
   [ 0.00000000, 0.17817762, 0.22459054 ],
   [ 0.00000000, 0.18054594, 0.22775855 ],
   [ 0.00000000, 0.18291426, 0.23092657 ],
   [ 0.00000000, 0.18528258, 0.23409458 ],
   [ 0.00000000, 0.18765090, 0.23726259 ],
   [ 0.00000000, 0.19001922, 0.24043060 ],
   [ 0.00000000, 0.19238754, 0.24359862 ],
   [ 0.00000000, 0.19475586, 0.24676663 ],
   [ 0.00000000, 0.19712418, 0.24993464 ],
   [ 0.00000000, 0.19949250, 0.25310265 ],
   [ 0.00000000, 0.20186082, 0.25627067 ],
   [ 0.00000000, 0.20422914, 0.25943868 ],
   [ 0.00000000, 0.20659746, 0.26260669 ],
   [ 0.00000000, 0.20896578, 0.26577470 ],
   [ 0.00000000, 0.21133410, 0.26894271 ],
   [ 0.00000000, 0.21370242, 0.27211073 ],
   [ 0.00000000, 0.21607074, 0.27527874 ],
   [ 0.00000000, 0.21843906, 0.27844675 ],
   [ 0.00000000, 0.22080738, 0.28161476 ],
   [ 0.00000000, 0.22317570, 0.28478278 ],
   [ 0.00000000, 0.22554402, 0.28795079 ],
   [ 0.00000000, 0.22791234, 0.29111880 ],
   [ 0.00000000, 0.23028066, 0.29428681 ],
   [ 0.00000000, 0.23264898, 0.29745483 ],
   [ 0.00000000, 0.23501730, 0.30062284 ],
   [ 0.00000000, 0.23738562, 0.30379085 ],
   [ 0.00000000, 0.23975394, 0.30695886 ],
   [ 0.00000000, 0.24212226, 0.31012687 ],
   [ 0.00000000, 0.24449058, 0.31329489 ],
   [ 0.00000000, 0.24685890, 0.31646290 ],
   [ 0.00000000, 0.24922722, 0.31963091 ],
   [ 0.00000000, 0.25159554, 0.32279892 ],
   [ 0.00000000, 0.25396386, 0.32596694 ],
   [ 0.00000000, 0.25633218, 0.32913495 ],
   [ 0.00000000, 0.25870050, 0.33230296 ],
   [ 0.00000000, 0.26106882, 0.33547097 ],
   [ 0.00000000, 0.26343714, 0.33863899 ],
   [ 0.00000000, 0.26580546, 0.34180700 ],
   [ 0.00000000, 0.26817378, 0.34497501 ],
   [ 0.00000000, 0.27054210, 0.34814302 ],
   [ 0.00000000, 0.27291042, 0.35131103 ],
   [ 0.00000000, 0.27527874, 0.35447905 ],
   [ 0.00000000, 0.27764706, 0.35764706 ],
   [ 0.00000000, 0.28001538, 0.36081507 ],
   [ 0.00000000, 0.28238370, 0.36398308 ],
   [ 0.00000000, 0.28475202, 0.36715110 ],
   [ 0.00000000, 0.28712034, 0.37031911 ],
   [ 0.00000000, 0.28948866, 0.37348712 ],
   [ 0.00000000, 0.29185698, 0.37665513 ],
   [ 0.00000000, 0.29422530, 0.37982314 ],
   [ 0.00000000, 0.29659362, 0.38299116 ],
   [ 0.00000000, 0.29896194, 0.38615917 ],
   [ 0.00000000, 0.30133026, 0.38932718 ],
   [ 0.00000000, 0.30369858, 0.39249519 ],
   [ 0.00000000, 0.30606690, 0.39566321 ],
   [ 0.00000000, 0.30843522, 0.39883122 ],
   [ 0.00000000, 0.31080354, 0.40199923 ],
   [ 0.00000000, 0.31317186, 0.40516724 ],
   [ 0.00000000, 0.31554018, 0.40833526 ],
   [ 0.00000000, 0.31790850, 0.41150327 ],
   [ 0.00000000, 0.32027682, 0.41467128 ],
   [ 0.00000000, 0.32264514, 0.41783929 ],
   [ 0.00000000, 0.32501346, 0.42100730 ],
   [ 0.00000000, 0.32738178, 0.42417532 ],
   [ 0.00000000, 0.32975010, 0.42734333 ],
   [ 0.00000000, 0.33211842, 0.43051134 ],
   [ 0.00000000, 0.33448674, 0.43367935 ],
   [ 0.00000000, 0.33685506, 0.43684737 ],
   [ 0.00000000, 0.33922338, 0.44001538 ],
   [ 0.00000000, 0.34159170, 0.44318339 ],
   [ 0.00000000, 0.34396002, 0.44635140 ],
   [ 0.00000000, 0.34632834, 0.44951942 ],
   [ 0.00000000, 0.34869666, 0.45268743 ],
   [ 0.00000000, 0.35106498, 0.45585544 ],
   [ 0.00000000, 0.35343329, 0.45902345 ],
   [ 0.00000000, 0.35580161, 0.46219146 ],
   [ 0.00000000, 0.35816993, 0.46535948 ],
   [ 0.00000000, 0.36053825, 0.46852749 ],
   [ 0.00000000, 0.36290657, 0.47169550 ],
   [ 0.00000000, 0.36527489, 0.47486351 ],
   [ 0.00000000, 0.36764321, 0.47803153 ],
   [ 0.00000000, 0.37001153, 0.48119954 ],
   [ 0.00000000, 0.37237985, 0.48436755 ],
   [ 0.00000000, 0.37474817, 0.48753556 ],
   [ 0.00000000, 0.37711649, 0.49070358 ],
   [ 0.00000000, 0.37948481, 0.49387159 ],
   [ 0.00000000, 0.38185313, 0.49703960 ],
   [ 0.00000000, 0.38422145, 0.50020761 ],
   [ 0.00000000, 0.38658977, 0.50337562 ],
   [ 0.00000000, 0.38895809, 0.50654364 ],
   [ 0.00000000, 0.39132641, 0.50971165 ],
   [ 0.00000000, 0.39369473, 0.51287966 ],
   [ 0.00000000, 0.39606305, 0.51604767 ],
   [ 0.00000000, 0.39843137, 0.51921569 ],
   [ 0.00000000, 0.40079969, 0.52238370 ],
   [ 0.00000000, 0.40316801, 0.52555171 ],
   [ 0.00000000, 0.40553633, 0.52871972 ],
   [ 0.00000000, 0.40790465, 0.53188774 ],
   [ 0.00000000, 0.41027297, 0.53505575 ],
   [ 0.00000000, 0.41264129, 0.53822376 ],
   [ 0.00000000, 0.41500961, 0.54139177 ],
   [ 0.00000000, 0.41737793, 0.54455978 ],
   [ 0.00000000, 0.41974625, 0.54772780 ],
   [ 0.00000000, 0.42211457, 0.55089581 ],
   [ 0.00000000, 0.42448289, 0.55406382 ],
   [ 0.00000000, 0.42685121, 0.55723183 ],
   [ 0.00000000, 0.42921953, 0.56039985 ],
   [ 0.00000000, 0.43158785, 0.56356786 ],
   [ 0.00000000, 0.43395617, 0.56673587 ],
   [ 0.00000000, 0.43632449, 0.56990388 ],
   [ 0.00000000, 0.43869281, 0.57307190 ],
   [ 0.00000000, 0.44106113, 0.57623991 ],
   [ 0.00000000, 0.44342945, 0.57940792 ],
   [ 0.00000000, 0.44579777, 0.58257593 ],
   [ 0.00000000, 0.44816609, 0.58574394 ],
   [ 0.00000000, 0.45053441, 0.58891196 ],
   [ 0.00000000, 0.45290273, 0.59207997 ],
   [ 0.00000000, 0.45527105, 0.59524798 ],
   [ 0.00000000, 0.45763937, 0.59841599 ],
   [ 0.00392157, 0.46040754, 0.59764706 ],
   [ 0.01176471, 0.46357555, 0.59294118 ],
   [ 0.01960784, 0.46674356, 0.58823529 ],
   [ 0.02745098, 0.46991157, 0.58352941 ],
   [ 0.03529412, 0.47307958, 0.57882353 ],
   [ 0.04313725, 0.47624760, 0.57411765 ],
   [ 0.05098039, 0.47941561, 0.56941176 ],
   [ 0.05882353, 0.48258362, 0.56470588 ],
   [ 0.06666667, 0.48575163, 0.56000000 ],
   [ 0.07450980, 0.48891965, 0.55529412 ],
   [ 0.08235294, 0.49208766, 0.55058824 ],
   [ 0.09019608, 0.49525567, 0.54588235 ],
   [ 0.09803922, 0.49842368, 0.54117647 ],
   [ 0.10588235, 0.50159170, 0.53647059 ],
   [ 0.11372549, 0.50475971, 0.53176471 ],
   [ 0.12156863, 0.50792772, 0.52705882 ],
   [ 0.12941176, 0.51109573, 0.52235294 ],
   [ 0.13725490, 0.51426374, 0.51764706 ],
   [ 0.14509804, 0.51743176, 0.51294118 ],
   [ 0.15294118, 0.52059977, 0.50823529 ],
   [ 0.16078431, 0.52376778, 0.50352941 ],
   [ 0.16862745, 0.52693579, 0.49882353 ],
   [ 0.17647059, 0.53010381, 0.49411765 ],
   [ 0.18431373, 0.53327182, 0.48941176 ],
   [ 0.19215686, 0.53643983, 0.48470588 ],
   [ 0.20000000, 0.53960784, 0.48000000 ],
   [ 0.20784314, 0.54277586, 0.47529412 ],
   [ 0.21568627, 0.54594387, 0.47058824 ],
   [ 0.22352941, 0.54911188, 0.46588235 ],
   [ 0.23137255, 0.55227989, 0.46117647 ],
   [ 0.23921569, 0.55544790, 0.45647059 ],
   [ 0.24705882, 0.55861592, 0.45176471 ],
   [ 0.25490196, 0.56178393, 0.44705882 ],
   [ 0.26274510, 0.56495194, 0.44235294 ],
   [ 0.27058824, 0.56811995, 0.43764706 ],
   [ 0.27843137, 0.57128797, 0.43294118 ],
   [ 0.28627451, 0.57445598, 0.42823529 ],
   [ 0.29411765, 0.57762399, 0.42352941 ],
   [ 0.30196078, 0.58079200, 0.41882353 ],
   [ 0.30980392, 0.58396002, 0.41411765 ],
   [ 0.31764706, 0.58712803, 0.40941176 ],
   [ 0.32549020, 0.59029604, 0.40470588 ],
   [ 0.33333333, 0.59346405, 0.40000000 ],
   [ 0.34117647, 0.59663206, 0.39529412 ],
   [ 0.34901961, 0.59980008, 0.39058824 ],
   [ 0.35686275, 0.60296809, 0.38588235 ],
   [ 0.36470588, 0.60613610, 0.38117647 ],
   [ 0.37254902, 0.60930411, 0.37647059 ],
   [ 0.38039216, 0.61247213, 0.37176471 ],
   [ 0.38823529, 0.61564014, 0.36705882 ],
   [ 0.39607843, 0.61880815, 0.36235294 ],
   [ 0.40392157, 0.62197616, 0.35764706 ],
   [ 0.41176471, 0.62514418, 0.35294118 ],
   [ 0.41960784, 0.62831219, 0.34823529 ],
   [ 0.42745098, 0.63148020, 0.34352941 ],
   [ 0.43529412, 0.63464821, 0.33882353 ],
   [ 0.44313725, 0.63781622, 0.33411765 ],
   [ 0.45098039, 0.64098424, 0.32941176 ],
   [ 0.45882353, 0.64415225, 0.32470588 ],
   [ 0.46666667, 0.64732026, 0.32000000 ],
   [ 0.47450980, 0.65048827, 0.31529412 ],
   [ 0.48235294, 0.65365629, 0.31058824 ],
   [ 0.49019608, 0.65682430, 0.30588235 ],
   [ 0.49803922, 0.65999231, 0.30117647 ],
   [ 0.50588235, 0.66316032, 0.29647059 ],
   [ 0.51372549, 0.66632834, 0.29176471 ],
   [ 0.52156863, 0.66949635, 0.28705882 ],
   [ 0.52941176, 0.67266436, 0.28235294 ],
   [ 0.53725490, 0.67583237, 0.27764706 ],
   [ 0.54509804, 0.67900038, 0.27294118 ],
   [ 0.55294118, 0.68216840, 0.26823529 ],
   [ 0.56078431, 0.68533641, 0.26352941 ],
   [ 0.56862745, 0.68850442, 0.25882353 ],
   [ 0.57647059, 0.69167243, 0.25411765 ],
   [ 0.58431373, 0.69484045, 0.24941176 ],
   [ 0.59215686, 0.69800846, 0.24470588 ],
   [ 0.60000000, 0.70117647, 0.24000000 ],
   [ 0.60784314, 0.70434448, 0.23529412 ],
   [ 0.61568627, 0.70751250, 0.23058824 ],
   [ 0.62352941, 0.71068051, 0.22588235 ],
   [ 0.63137255, 0.71384852, 0.22117647 ],
   [ 0.63921569, 0.71701653, 0.21647059 ],
   [ 0.64705882, 0.72018454, 0.21176471 ],
   [ 0.65490196, 0.72335256, 0.20705882 ],
   [ 0.66274510, 0.72652057, 0.20235294 ],
   [ 0.67058824, 0.72968858, 0.19764706 ],
   [ 0.67843137, 0.73285659, 0.19294118 ],
   [ 0.68627451, 0.73602461, 0.18823529 ],
   [ 0.69411765, 0.73919262, 0.18352941 ],
   [ 0.70196078, 0.74236063, 0.17882353 ],
   [ 0.70980392, 0.74552864, 0.17411765 ],
   [ 0.71764706, 0.74869666, 0.16941176 ],
   [ 0.72549020, 0.75186467, 0.16470588 ],
   [ 0.73333333, 0.75503268, 0.16000000 ],
   [ 0.74117647, 0.75820069, 0.15529412 ],
   [ 0.74901961, 0.76136870, 0.15058824 ],
   [ 0.75686275, 0.76453672, 0.14588235 ],
   [ 0.76470588, 0.76770473, 0.14117647 ],
   [ 0.77254902, 0.77087274, 0.13647059 ],
   [ 0.78039216, 0.77404075, 0.13176471 ],
   [ 0.78823529, 0.77720877, 0.12705882 ],
   [ 0.79607843, 0.78037678, 0.12235294 ],
   [ 0.80392157, 0.78354479, 0.11764706 ],
   [ 0.81176471, 0.78671280, 0.11294118 ],
   [ 0.81960784, 0.78988082, 0.10823529 ],
   [ 0.82745098, 0.79304883, 0.10352941 ],
   [ 0.83529412, 0.79621684, 0.09882353 ],
   [ 0.84313725, 0.79938485, 0.09411765 ],
   [ 0.85098039, 0.80255286, 0.08941176 ],
   [ 0.85882353, 0.80572088, 0.08470588 ],
   [ 0.86666667, 0.80888889, 0.08000000 ],
   [ 0.87450980, 0.81205690, 0.07529412 ],
   [ 0.88235294, 0.81522491, 0.07058824 ],
   [ 0.89019608, 0.81839293, 0.06588235 ],
   [ 0.89803922, 0.82156094, 0.06117647 ],
   [ 0.90588235, 0.82472895, 0.05647059 ],
   [ 0.91372549, 0.82789696, 0.05176471 ],
   [ 0.92156863, 0.83106498, 0.04705882 ],
   [ 0.92941176, 0.83423299, 0.04235294 ],
   [ 0.93725490, 0.83740100, 0.03764706 ],
   [ 0.94509804, 0.84056901, 0.03294118 ],
   [ 0.95294118, 0.84373702, 0.02823529 ],
   [ 0.96078431, 0.84690504, 0.02352941 ],
   [ 0.96862745, 0.85007305, 0.01882353 ],
   [ 0.97647059, 0.85324106, 0.01411765 ],
   [ 0.98431373, 0.85640907, 0.00941176 ],
   [ 0.99215686, 0.85957709, 0.00470588 ],
   [ 1.00000000, 0.86274510, 0.00000000 ],
]

_luts = [ _bam_viridis_lut ]
_names = [ 'bam_viridis' ]

for _lut, _name in zip(_luts, _names):

    _cmap = colors.ListedColormap(_lut, _name) 
    locals()[_name] = _cmap

    _cmap_r = colors.ListedColormap(_lut[::-1], _name + "_r")  
    locals()[_name + "_r"] = _cmap_r

    mpl_cm.register_cmap(_name, _cmap)
    mpl_cm.register_cmap(_name + "_r", _cmap_r)