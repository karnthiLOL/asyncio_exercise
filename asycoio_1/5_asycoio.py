#example of waiting for all tasks to complete
import random
import asyncio
import time

#corotine to execute in a new task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = random.random()
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

#main corotine
async def main():
    #create many task
    tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
    #wait for all tasks to complete #ALL_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    #report result
    print(f'{time.ctime()} All done')

#start the asyncio program
asyncio.run(main())


##Result
#FIRST_COMPLETED
# Wed Jul 12 15:03:44 2023 >task 44 done with 0.0078414028966719
# Wed Jul 12 15:03:44 2023 All done

#FIRST_EXCEPTION
# Wed Jul 12 15:04:43 2023 >task 18 done with 0.0012433961619058298
# Wed Jul 12 15:04:43 2023 >task 51 done with 0.010164094145691416
# Wed Jul 12 15:04:43 2023 >task 48 done with 0.016928778841853842
# Wed Jul 12 15:04:43 2023 >task 17 done with 0.022318305321685328
# Wed Jul 12 15:04:43 2023 >task 58 done with 0.026587595265531783
# Wed Jul 12 15:04:43 2023 >task 14 done with 0.03118822424082024
# Wed Jul 12 15:04:43 2023 >task 72 done with 0.03450343547054158
# Wed Jul 12 15:04:43 2023 >task 90 done with 0.035970229553267674
# Wed Jul 12 15:04:43 2023 >task 32 done with 0.04599727088660155
# Wed Jul 12 15:04:43 2023 >task 46 done with 0.05759104410271987
# Wed Jul 12 15:04:43 2023 >task 77 done with 0.06545846237989117
# Wed Jul 12 15:04:43 2023 >task 28 done with 0.07374873305496121
# Wed Jul 12 15:04:43 2023 >task 62 done with 0.08263930403320907
# Wed Jul 12 15:04:43 2023 >task 76 done with 0.12190664346824553
# Wed Jul 12 15:04:43 2023 >task 20 done with 0.1299951162948546
# Wed Jul 12 15:04:43 2023 >task 83 done with 0.1380888586235608
# Wed Jul 12 15:04:43 2023 >task 61 done with 0.15229075496656153
# Wed Jul 12 15:04:43 2023 >task 67 done with 0.15450744943087302
# Wed Jul 12 15:04:43 2023 >task 43 done with 0.16571759099150085
# Wed Jul 12 15:04:43 2023 >task 55 done with 0.17667799889727354
# Wed Jul 12 15:04:43 2023 >task 97 done with 0.17834124792032213
# Wed Jul 12 15:04:43 2023 >task 47 done with 0.17987922018198055
# Wed Jul 12 15:04:43 2023 >task 16 done with 0.1882024004160363
# Wed Jul 12 15:04:43 2023 >task 93 done with 0.18820260315780213
# Wed Jul 12 15:04:43 2023 >task 60 done with 0.1890291785068553
# Wed Jul 12 15:04:43 2023 >task 54 done with 0.19928798703936912
# Wed Jul 12 15:04:43 2023 >task 37 done with 0.20541187191453425
# Wed Jul 12 15:04:43 2023 >task 39 done with 0.21040932709530924
# Wed Jul 12 15:04:43 2023 >task 13 done with 0.22150904218753387
# Wed Jul 12 15:04:43 2023 >task 25 done with 0.22991657907299656
# Wed Jul 12 15:04:44 2023 >task 65 done with 0.24801170021370478
# Wed Jul 12 15:04:44 2023 >task 94 done with 0.25193417918901206
# Wed Jul 12 15:04:44 2023 >task 52 done with 0.2776113643236936
# Wed Jul 12 15:04:44 2023 >task 80 done with 0.28408301680748715
# Wed Jul 12 15:04:44 2023 >task 68 done with 0.3172807123366326
# Wed Jul 12 15:04:44 2023 >task 22 done with 0.34128149650281137
# Wed Jul 12 15:04:44 2023 >task 2 done with 0.3448159918993424
# Wed Jul 12 15:04:44 2023 >task 31 done with 0.3461280397284432
# Wed Jul 12 15:04:44 2023 >task 49 done with 0.3522282011591519
# Wed Jul 12 15:04:44 2023 >task 30 done with 0.35524445170305774
# Wed Jul 12 15:04:44 2023 >task 6 done with 0.35703437263423543
# Wed Jul 12 15:04:44 2023 >task 63 done with 0.3654394531417633
# Wed Jul 12 15:04:44 2023 >task 56 done with 0.38523720943159845
# Wed Jul 12 15:04:44 2023 >task 87 done with 0.3886962340374589
# Wed Jul 12 15:04:44 2023 >task 71 done with 0.40280996219094445
# Wed Jul 12 15:04:44 2023 >task 57 done with 0.4080047586836638
# Wed Jul 12 15:04:44 2023 >task 69 done with 0.4133659417837795
# Wed Jul 12 15:04:44 2023 >task 40 done with 0.4190914097819446
# Wed Jul 12 15:04:44 2023 >task 36 done with 0.42262493217996955
# Wed Jul 12 15:04:44 2023 >task 85 done with 0.4247629783584831
# Wed Jul 12 15:04:44 2023 >task 23 done with 0.4274970301361277
# Wed Jul 12 15:04:44 2023 >task 98 done with 0.4298299446224878
# Wed Jul 12 15:04:44 2023 >task 44 done with 0.43040487624596224
# Wed Jul 12 15:04:44 2023 >task 33 done with 0.44314106752431626
# Wed Jul 12 15:04:44 2023 >task 7 done with 0.44952345123186943
# Wed Jul 12 15:04:44 2023 >task 41 done with 0.487502093744838
# Wed Jul 12 15:04:44 2023 >task 75 done with 0.49628488429256157
# Wed Jul 12 15:04:44 2023 >task 9 done with 0.5161147184114872
# Wed Jul 12 15:04:44 2023 >task 59 done with 0.5190096342681939
# Wed Jul 12 15:04:44 2023 >task 73 done with 0.5321516771971395
# Wed Jul 12 15:04:44 2023 >task 95 done with 0.5355457010864635
# Wed Jul 12 15:04:44 2023 >task 86 done with 0.5381234848810579
# Wed Jul 12 15:04:44 2023 >task 50 done with 0.5480704835238371
# Wed Jul 12 15:04:44 2023 >task 79 done with 0.5506342615812204
# Wed Jul 12 15:04:44 2023 >task 15 done with 0.5531045108772281
# Wed Jul 12 15:04:44 2023 >task 3 done with 0.5544541696500462
# Wed Jul 12 15:04:44 2023 >task 11 done with 0.5601375147080758
# Wed Jul 12 15:04:44 2023 >task 0 done with 0.5670801012883331
# Wed Jul 12 15:04:44 2023 >task 27 done with 0.5692232411252447
# Wed Jul 12 15:04:44 2023 >task 12 done with 0.5732696283344949
# Wed Jul 12 15:04:44 2023 >task 70 done with 0.5791456558693421
# Wed Jul 12 15:04:44 2023 >task 96 done with 0.5824945074731995
# Wed Jul 12 15:04:44 2023 >task 10 done with 0.5828761156226445
# Wed Jul 12 15:04:44 2023 >task 42 done with 0.6136641059238724
# Wed Jul 12 15:04:44 2023 >task 45 done with 0.6142058827942329
# Wed Jul 12 15:04:44 2023 >task 92 done with 0.620376748268732
# Wed Jul 12 15:04:44 2023 >task 19 done with 0.6296158768288996
# Wed Jul 12 15:04:44 2023 >task 34 done with 0.6504501433613057
# Wed Jul 12 15:04:44 2023 >task 81 done with 0.6659634838981037
# Wed Jul 12 15:04:44 2023 >task 5 done with 0.6736389083559264
# Wed Jul 12 15:04:44 2023 >task 21 done with 0.6870358067891158
# Wed Jul 12 15:04:44 2023 >task 99 done with 0.6903762967744179
# Wed Jul 12 15:04:44 2023 >task 84 done with 0.6971693645098086
# Wed Jul 12 15:04:44 2023 >task 74 done with 0.7547220598265892
# Wed Jul 12 15:04:44 2023 >task 1 done with 0.7963199898331691
# Wed Jul 12 15:04:44 2023 >task 8 done with 0.8149340928018582
# Wed Jul 12 15:04:44 2023 >task 64 done with 0.8183553568166754
# Wed Jul 12 15:04:44 2023 >task 35 done with 0.8451091602248829
# Wed Jul 12 15:04:44 2023 >task 24 done with 0.8742162903096762
# Wed Jul 12 15:04:44 2023 >task 78 done with 0.880065614399068
# Wed Jul 12 15:04:44 2023 >task 66 done with 0.8827641420588199
# Wed Jul 12 15:04:44 2023 >task 89 done with 0.8867955683228479
# Wed Jul 12 15:04:44 2023 >task 53 done with 0.9091792136696456
# Wed Jul 12 15:04:44 2023 >task 4 done with 0.9336205322377398
# Wed Jul 12 15:04:44 2023 >task 88 done with 0.9414101976013116
# Wed Jul 12 15:04:44 2023 >task 26 done with 0.9632455017942303
# Wed Jul 12 15:04:44 2023 >task 82 done with 0.9677662689404218
# Wed Jul 12 15:04:44 2023 >task 29 done with 0.9746732417414574
# Wed Jul 12 15:04:44 2023 >task 91 done with 0.9880847386899944
# Wed Jul 12 15:04:44 2023 >task 38 done with 0.9897261705660318
# Wed Jul 12 15:04:44 2023 All done

#ALL_COMPLETED
# Wed Jul 12 15:05:27 2023 >task 29 done with 0.006763550611101898
# Wed Jul 12 15:05:27 2023 >task 19 done with 0.011329342507666817
# Wed Jul 12 15:05:27 2023 >task 11 done with 0.015917446358544973
# Wed Jul 12 15:05:27 2023 >task 88 done with 0.046902603951990085
# Wed Jul 12 15:05:27 2023 >task 82 done with 0.050792881771448695
# Wed Jul 12 15:05:27 2023 >task 52 done with 0.061073147130052186
# Wed Jul 12 15:05:27 2023 >task 5 done with 0.0704815137418886
# Wed Jul 12 15:05:27 2023 >task 25 done with 0.07762958583541191
# Wed Jul 12 15:05:27 2023 >task 44 done with 0.08276149131412791
# Wed Jul 12 15:05:27 2023 >task 38 done with 0.088015307524683
# Wed Jul 12 15:05:27 2023 >task 92 done with 0.09215195161963152
# Wed Jul 12 15:05:27 2023 >task 57 done with 0.11354328366525535
# Wed Jul 12 15:05:27 2023 >task 10 done with 0.12351224323354149
# Wed Jul 12 15:05:27 2023 >task 54 done with 0.12546888181200966
# Wed Jul 12 15:05:27 2023 >task 65 done with 0.13189085506628428
# Wed Jul 12 15:05:27 2023 >task 21 done with 0.1322047278784767
# Wed Jul 12 15:05:27 2023 >task 81 done with 0.13741551217508363
# Wed Jul 12 15:05:27 2023 >task 60 done with 0.16076267744988448
# Wed Jul 12 15:05:27 2023 >task 24 done with 0.16267223396699648
# Wed Jul 12 15:05:27 2023 >task 40 done with 0.1659014014996668
# Wed Jul 12 15:05:27 2023 >task 14 done with 0.1670333156886329
# Wed Jul 12 15:05:27 2023 >task 73 done with 0.19469935167916208
# Wed Jul 12 15:05:27 2023 >task 20 done with 0.2068835927445366
# Wed Jul 12 15:05:27 2023 >task 76 done with 0.2147697517741478
# Wed Jul 12 15:05:27 2023 >task 37 done with 0.21731840567530314
# Wed Jul 12 15:05:27 2023 >task 83 done with 0.21860089753423573
# Wed Jul 12 15:05:27 2023 >task 68 done with 0.22506404290121684
# Wed Jul 12 15:05:27 2023 >task 72 done with 0.24500041820839913
# Wed Jul 12 15:05:27 2023 >task 3 done with 0.2611839924707444
# Wed Jul 12 15:05:27 2023 >task 50 done with 0.28505639127051097
# Wed Jul 12 15:05:27 2023 >task 66 done with 0.2871453991865244
# Wed Jul 12 15:05:27 2023 >task 47 done with 0.28814078183341707
# Wed Jul 12 15:05:27 2023 >task 22 done with 0.2979663695127235
# Wed Jul 12 15:05:27 2023 >task 69 done with 0.3061330258722177
# Wed Jul 12 15:05:27 2023 >task 84 done with 0.3139161303069151
# Wed Jul 12 15:05:27 2023 >task 15 done with 0.3182455397047408
# Wed Jul 12 15:05:27 2023 >task 75 done with 0.3224383501321286
# Wed Jul 12 15:05:27 2023 >task 93 done with 0.40251137032279394
# Wed Jul 12 15:05:27 2023 >task 59 done with 0.40793601110824196
# Wed Jul 12 15:05:27 2023 >task 39 done with 0.4164308552274253
# Wed Jul 12 15:05:27 2023 >task 90 done with 0.4166030187308708
# Wed Jul 12 15:05:27 2023 >task 12 done with 0.4375499359855596
# Wed Jul 12 15:05:27 2023 >task 63 done with 0.4405291065897793
# Wed Jul 12 15:05:27 2023 >task 97 done with 0.46955391796680923
# Wed Jul 12 15:05:27 2023 >task 32 done with 0.4730421414562399
# Wed Jul 12 15:05:27 2023 >task 86 done with 0.49082194354703557
# Wed Jul 12 15:05:27 2023 >task 87 done with 0.49418412600303674
# Wed Jul 12 15:05:28 2023 >task 74 done with 0.5088452601412962
# Wed Jul 12 15:05:28 2023 >task 89 done with 0.5162070367419612
# Wed Jul 12 15:05:28 2023 >task 64 done with 0.5399234475334557
# Wed Jul 12 15:05:28 2023 >task 7 done with 0.5461505747790726
# Wed Jul 12 15:05:28 2023 >task 27 done with 0.5467623987569117
# Wed Jul 12 15:05:28 2023 >task 13 done with 0.5647816469660286
# Wed Jul 12 15:05:28 2023 >task 0 done with 0.5715930835045118
# Wed Jul 12 15:05:28 2023 >task 61 done with 0.5716242119702986
# Wed Jul 12 15:05:28 2023 >task 80 done with 0.5772124838166826
# Wed Jul 12 15:05:28 2023 >task 91 done with 0.5774755168378755
# Wed Jul 12 15:05:28 2023 >task 67 done with 0.5791110785696175
# Wed Jul 12 15:05:28 2023 >task 30 done with 0.5799562467137593
# Wed Jul 12 15:05:28 2023 >task 71 done with 0.6184255366814759
# Wed Jul 12 15:05:28 2023 >task 51 done with 0.6368741377804076
# Wed Jul 12 15:05:28 2023 >task 9 done with 0.6409709986307455
# Wed Jul 12 15:05:28 2023 >task 78 done with 0.6509069591844048
# Wed Jul 12 15:05:28 2023 >task 23 done with 0.661149568482546
# Wed Jul 12 15:05:28 2023 >task 1 done with 0.6613538253210494
# Wed Jul 12 15:05:28 2023 >task 85 done with 0.6654449950881426
# Wed Jul 12 15:05:28 2023 >task 49 done with 0.6735156789387328
# Wed Jul 12 15:05:28 2023 >task 62 done with 0.6766731636784933
# Wed Jul 12 15:05:28 2023 >task 28 done with 0.6962719012587124
# Wed Jul 12 15:05:28 2023 >task 79 done with 0.6964076108416001
# Wed Jul 12 15:05:28 2023 >task 56 done with 0.6993847919960012
# Wed Jul 12 15:05:28 2023 >task 26 done with 0.7155159739379097
# Wed Jul 12 15:05:28 2023 >task 98 done with 0.7219735673911224
# Wed Jul 12 15:05:28 2023 >task 42 done with 0.7341375767660805
# Wed Jul 12 15:05:28 2023 >task 94 done with 0.735725515918412
# Wed Jul 12 15:05:28 2023 >task 18 done with 0.7419459950421641
# Wed Jul 12 15:05:28 2023 >task 46 done with 0.7610188982861769
# Wed Jul 12 15:05:28 2023 >task 48 done with 0.7756744978142693
# Wed Jul 12 15:05:28 2023 >task 70 done with 0.8017606482947888
# Wed Jul 12 15:05:28 2023 >task 17 done with 0.8048876096936108
# Wed Jul 12 15:05:28 2023 >task 53 done with 0.8226941482261867
# Wed Jul 12 15:05:28 2023 >task 31 done with 0.8291704591236726
# Wed Jul 12 15:05:28 2023 >task 2 done with 0.8377165668961251
# Wed Jul 12 15:05:28 2023 >task 58 done with 0.8392823512684754
# Wed Jul 12 15:05:28 2023 >task 41 done with 0.8597094664736643
# Wed Jul 12 15:05:28 2023 >task 99 done with 0.8659051989880773
# Wed Jul 12 15:05:28 2023 >task 95 done with 0.8800836554643743
# Wed Jul 12 15:05:28 2023 >task 4 done with 0.8911849108198394
# Wed Jul 12 15:05:28 2023 >task 8 done with 0.9016615123488738
# Wed Jul 12 15:05:28 2023 >task 43 done with 0.9060614056035265
# Wed Jul 12 15:05:28 2023 >task 35 done with 0.915115489877076
# Wed Jul 12 15:05:28 2023 >task 34 done with 0.9182609699623439
# Wed Jul 12 15:05:28 2023 >task 16 done with 0.9280671662535246
# Wed Jul 12 15:05:28 2023 >task 33 done with 0.9461562525656668
# Wed Jul 12 15:05:28 2023 >task 55 done with 0.9481259345526375
# Wed Jul 12 15:05:28 2023 >task 96 done with 0.9530435688604348
# Wed Jul 12 15:05:28 2023 >task 6 done with 0.9534940510610541
# Wed Jul 12 15:05:28 2023 >task 77 done with 0.9727935490871545
# Wed Jul 12 15:05:28 2023 >task 45 done with 0.977780296719653
# Wed Jul 12 15:05:28 2023 >task 36 done with 0.9978468896658479
# Wed Jul 12 15:05:28 2023 All done