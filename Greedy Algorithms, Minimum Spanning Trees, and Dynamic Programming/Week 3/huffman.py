import os
from collections import defaultdict
from heapq import heapify,heappop,heappush

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
d = 'Huffman.txt'

with open(d, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    no_of_nodes,nodes_weight = '1000',[]
    count = 1
    for line in infile.readlines():

        if int(line)==1000:
            pass
            
        else:
            nodes_weight.append((int(line),str(count),0,0))
            count+=1

def Huffman(d):

    mergeds = {}
    max_count = 0
    heapify(d)
    

    while len(d)>1:
    
        a,b = heappop(d),heappop(d)
#   
 
        weight = a[0]+b[0]
        name = a[1]+'_'+b[1]
        max_len = a[2]+b[2]
        min_len = a[3]+b[3]
        
        if len(mergeds)==0:
            
            merged = (weight,1,1)
            mergeds[name] = merged
        
        elif a[1] in mergeds and b[1] not in mergeds:
#             
            merged = (weight,mergeds[a[1]][1]+1,1)
            mergeds[name] = merged
            
        elif b[1] in mergeds and a[1] not in mergeds:
#             
            merged = (weight,mergeds[b[1]][1]+1,1)
            mergeds[name] = merged
        
        elif a[1] not in mergeds and b[1] not in mergeds:
#        
            merged = (weight,1,1)
            mergeds[name] = merged
        
        elif a[1] in mergeds and b[1] in mergeds:
#        
            merged = (weight,max(a[2]+1,b[2]+1),min(a[-1]+1,b[-1]+1))
            mergeds[name] = merged
        
        weight,mmax,mmin = merged[0],merged[1],merged[2]
        
        heappush(d,(weight,name,mmax,mmin))
    # supernode = 
        
    return mergeds['392_614_62_280_725_989_700_690_413_571_143_49_618_787_353_507_866_915_664_679_85_862_452_356_199_632_380_536_826_750_17_584_208_59_281_1_520_907_157_428_176_653_569_939_611_95_558_523_528_833_847_432_287_212_445_197_509_547_678_96_889_815_458_627_395_114_773_331_838_326_510_874_293_903_415_332_19_991_352_890_776_495_650_525_45_93_617_224_741_444_517_162_647_615_407_299_910_463_108_301_448_146_719_167_660_188_527_911_818_277_117_711_712_173_236_756_670_292_494_429_901_967_530_156_241_762_846_891_843_404_218_205_564_593_609_468_727_451_993_4_170_914_699_856_736_40_850_766_469_313_976_636_821_908_696_140_738_587_113_754_182_694_56_505_237_534_778_665_508_294_141_502_462_298_370_443_620_555_868_805_962_931_368_590_52_133_101_144_53_978_740_213_685_952_546_663_82_442_57_124_154_20_605_231_562_742_130_51_577_187_14_229_759_808_608_631_777_202_872_918_270_160_982_786_583_758_377_291_481_177_235_894_675_384_412_137_500_785_118_543_24_837_626_438_592_858_209_801_767_922_996_41_830_659_414_243_633_10_794_459_35_779_44_925_921_586_578_436_848_667_26_486_357_958_879_603_478_273_686_706_150_222_339_282_245_684_423_693_946_16_729_864_999_54_651_501_310_230_309_398_39_371_998_266_437_275_885_125_200_87_789_43_70_256_239_943_289_296_178_844_721_348_456_259_745_553_623_467_134_798_576_646_193_189_718_196_709_588_492_744_835_747_873_728_630_537_871_285_545_399_450_135_304_321_832_606_842_888_232_86_336_324_726_67_972_175_406_511_77_792_323_995_957_441_12_457_420_226_1000_13_582_408_92_138_980_184_810_804_402_274_836_104_317_681_575_214_764_396_607_159_770_440_257_724_78_136_244_148_417_42_31_559_397_853_566_302_181_234_115_619_145_912_279_795_861_338_103_983_710_89_598_960_563_105_422_303_610_373_755_283_360_716_375_761_476_171_771_568_540_769_791_215_435_250_522_127_389_426_58_954_735_390_288_168_934_544_526_238_419_680_994_902_369_860_131_46_875_183_322_519_516_883_661_524_109_480_110_557_697_884_123_813_532_948_425_363_720_403_430_823_37_424_128_644_529_320_702_774_979_483_431_897_877_142_139_88_120_734_497_106_34_781_580_47_367_688_515_343_27_616_654_319_701_757_942_964_465_595_784_381_147_401_682_461_992_38_340_743_637_878_929_155_984_552_433_945_896_987_924_666_68_905_198_203_887_186_596_589_6_362_570_487_657_409_394_506_731_119_886_223_642_839_308_374_366_851_272_600_512_228_100_775_876_809_572_316_634_379_5_169_194_149_98_434_880_328_327_652_276_909_258_411_763_641_55_247_18_551_471_622_597_474_840_807_828_514_561_9_990_687_132_604_174_354_410_968_935_969_111_656_190_732_29_811_227_783_893_768_32_261_161_253_210_102_499_347_730_269_479_658_163_717_477_191_802_913_538_579_865_99_242_365_668_704_84_204_829_548_531_73_454_708_355_601_262_949_66_765_460_793_284_25_295_919_649_672_981_772_643_599_383_449_472_799_753_211_937_953_824_427_233_624_225_8_79_812_90_418_591_297_50_185_715_950_393_565_973_446_882_676_23_358_852_206_855_749_780_645_491_305_854_859_628_60_64_904_692_655_386_201_264_988_312_849_926_796_195_895_825_74_180_790_560_221_834_746_820_997_351_207_803_612_669_333_30_306_573_951_378_290_158_278_152_334_216_179_307_733_165_722_496_648_346_662_240_65_153_933_107_689_97_985_263_814_349_841_955_940_248_923_737_112_300_493_941_498_164_350_439_713_806_15_470_831_986_705_75_3_466_416_318_966_542_892_473_335_956_797_691_961_928_267_63_94_490_315_554_400_752_382_845_800_927_314_249_671_900_385_541_286_594_677_581_485_827_48_714_345_28_69_91_635_447_625_975_268_265_521_254_621_376_574_974_387_723_695_549_121_71_977_707_535_673_556_219_489_613_2_920_337_751_455_72_567_359_484_683_817_585_899_217_739_475_870_639_260_464_61_330_629_421_703_965_916_944_344_129_947_539_372_881_122_22_405_7_33_518_550_391_760_698_76_788_116_959_311_388_271_341_151_816_917_930_192_819_898_36_81_748_869_857_938_863_488_504_971_482_822_963_364_361_11_640_638_329_21_166_674_782_936_126_83_251_932_252_220_602_342_255_906_533_513_80_453_246_867_172_325_970_503']
#     elif a or b


print(Huffman(nodes_weight))

