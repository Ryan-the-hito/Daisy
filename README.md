# 🌼Daisy: Ambient Light Reminder and Auto-switcher

![65ldrAT](https://i.imgur.com/65ldrAT.png)

<p align="center"><a href="README.md">English</a> | <a href="README_cn.md">简体中文</a></p>

<p align="center"><a href="https://t.me/+AODLypeF_aYwYjNh">Telegram</a> | <a href="https://twitter.com/ryanswindows">Twitter</a> | <a href="https://weibo.com/ryanthehitos">Weibo</a></p>

Daisy 是一个 macOS 上的 app，用来提醒用户环境光过明或过暗，以及（在 Pro 版本中）自动调节环境亮度，以达到护眼的目的。

## 解决问题

对于长期需要对着电脑屏幕的人群来说，护眼是一个非常急切，也是名目繁多的议题。除了系统自带的 Night Shift、True Tone，第三方软件还能监测用眼时间、冷暖光调整、屏幕亮度调整、明暗主题调整……在这些众多功能中，我自己的使用感受是：**护眼的重点可能不在“明暗主题”或者“冷暖色调”，而在于两点，一是用眼时间，二是环境光线**。那么是不是说明暗与冷暖的功能完全没有利好呢？倒也不是。冷暖比较好理解，但是市面上也有带过滤功能的屏幕膜，做到硬件级的 24 小时过滤，软件端的似乎不那么必要。若不谈这些产品是否真正有效，另一个影响因素是，改变冷暖光影响了屏幕显色。对于时常需要摄影和修图的人来说，这反而增加了日常困难。至于明暗主题，我个人觉得其初衷未必是护眼。暗主题深色底配白字，确实是显得屏幕上的文字更清晰了，但是稍微看一段时间，眼睛就会花，字会糊在一起……更清晰的代价可能是用眼更费劲。所以，要实现生活需求和护眼需求的平衡，一方面是减少用眼时间，另一方面其实主要是保证环境光不至于太暗或者太亮，使单位时间内用眼更轻松。而后者似乎没有什么软件产品，因此我打算做一个这样的产品。

另一个动因是，Mac 上已经有一些成熟的第三方噪音检测软件，可以提示使用者是否暴露在较大噪音的环境。我之前也写过一个软件——[Cherry](https://github.com/Ryan-the-hito/Cherry)，用来调整系统音量高低变化，防止声音过高或者过低。声音方面尚兼有针对环境和系统的产品，但是在光线管理方面，几乎很少见到针对环境的工具。f.lux 确实有环境光管理，只不过那还是调整环境光的冷暖，而不是亮度。我希望这个产品能一方面吸取提醒类工具的长项，另一方面稍微补足光线管理在环境自动化领域的应用。

## 功能亮点

### 环境光提醒（基本功能）：

正如所有提醒类软件一样，Daisy 的首要功能是在环境光太暗和太亮的时候提醒用户。Mac 在很多机型上设有环境光传感器。但是 Daisy 没有通过这个方式获取环境光亮度。Daisy 的目的不是干掉其他软件和系统功能，而是希望和其他功能一起运行。macOS 如果内置了跟随环境光自动调节亮度，那么用户可以首先多一个“根据环境光自动调节屏幕亮度的功能”。但是系统的功能不具备提醒功能，仅仅是调整亮度。因此，Daisy 将太暗被设置为 20% 的屏幕亮度，太亮则是 90%。如果随环境光变化的屏幕亮度低于 20% 或者高于90%，那么会触发 Daisy，提醒用户根据现有情况调整环境光线的强度。

### 自动调节环境光（高级功能）：

如果用户还有智能设备——例如作为照明的智能台灯，用户可将其接入 Home，Daisy 还可以通过快捷指令（Shortcuts）发出指令，调整该智能设备的亮度：当环境光较暗时，将该设备的亮度调高 10%-20%，反之亦然。

## 界面一览

<p align="center">
  <img src="https://i.imgur.com/1Huutz9.png" width=400 />
</p>

Daisy 没有主界面，只有设置界面。在此界面中，第一行可设置 Daisy 每隔多少秒检测一次。默认设置为每 30 秒检测一次。此功能为基本功能，免费版和付费版中均有包含。

第二个和第三个设置项都是付费版内容。其中，第二个设置可以客制光线亮度的范围，决定临界值。第三个设置则是可选的，用户可自行决定是否打开运行快捷指令的选项。如果打开的话，那么 Daisy 就会在对应的情况下执行对应的快捷指令。用户应在对应情况后的栏目中写上对应快捷指令的名称。默认情况下，太暗情景下的指令为“DarkTime-BrightnessUp”，太亮情景下的则为“BrightTime-BrightnessDown”。如果修改这些设置，请记得点击 Save 保存设置。上文提到的指令集可以在下文获得默认模板。

提醒时的界面：

<p align="center">
  <img src="https://i.imgur.com/8CrVApk.png" width=400 />
</p>

如果开启了自动调节的话，那么 Daisy 不仅会提醒亮度，还会在调整环境灯亮度前后发出提醒：

<p align="center">
  <img src="https://i.imgur.com/KThHm7N.png" width=400 />
</p>

在我电脑上运行约 24 小时后的耗电情况（挺节能的，耗电很少）：

<p align="center">
  <img src="https://i.imgur.com/6OsBRWb.png" width=400 />
</p>

免费版和付费版的“设置”（Settings）板块：

<p align="center">
  <img src="https://i.imgur.com/hiy7G6L.png" width=400 />
  <img src="https://i.imgur.com/1Huutz9.png" width=400 />
</p>

免费版和付费版的“关于”（About）板块：

<p align="center">
  <img src="https://i.imgur.com/MYBzu5S.png" width=400 />
  <img src="https://i.imgur.com/qAZo8rN.png" width=400 />
</p>

## DEMO

https://github.com/Ryan-the-hito/Daisy/assets/95213517/fd4c2fc9-f1a2-4199-9576-cb6809f4ab1c

## 环境要求

- MacOS 12 Monterey 及以上（测试环境为 MacOS 12.6.5）
- M1、M2 芯片
- 网络环境自理

## 类型价目

|      | 免费版                      | 付费版                      |
|------|-----------------------------|-----------------------------|
| 基本功能 |1. 环境光过暗或者过亮时提醒<br>2. 设置自动检测环境光的间隔时间 | 1. 环境光过暗或者过亮时提醒<br>2. 设置自动检测环境光的间隔时间|
| 高级功能 | 无 | 3. 自定义过暗和过亮的亮度范围<br>4. 过暗或者过亮时自动执行快捷指令，自动调节 Home 中的智能灯亮度|
| 价格 | 免费                        | $1（只要一美元哦）      |
| 获取 | [Github Releases](https://github.com/Ryan-the-hito/Daisy/releases)<br>[Google Drive](https://drive.google.com/drive/folders/1sqAwRH-3suDPkl_GV78qW_-BklWU20Ru?usp=drive_link)<br>[Baidu Netdisk](https://pan.baidu.com/s/1dW27Pi_Fi-BhyZTMTzBzag?pwd=75q3)<br>[Dropbox](https://www.dropbox.com/scl/fo/nrn30qjqffsebrzlkxilv/h?rlkey=09vmwun931k3ugw0j1qd8njpa&dl=0)  | [点击购买](https://www.buymeacoffee.com/ryanthehito/e/155171) |

## 下载安装

1. **第一步：下载软件**：从 Release 中下载软件的压缩文件，解压后拖至系统程序文件夹；
2. **第二步：设置检测**：打开系统设置（System Preferences 或者 System Settings），在显示（Display）板块，勾选自动调整亮度的功能，如下图所示：
   <p align="center">
	<img src="https://i.imgur.com/TPa11q3.png" width=400 />
	</p>
   打开之后，电脑屏幕的亮度就会自动地由系统管理，因此不建议手动调整电脑屏幕，而是通过调整环境光的角度和亮度来实现良好的办公环境。许多用户因为自动亮度太低而是手动拉高屏幕亮度值，但是这恰恰是伤眼的——这说明用户此时身处一个环境光较暗的空间，但是相反却使用较高亮度的屏幕，对眼睛的压力会更大。除非特殊情况，否则将屏幕亮度调至低于 20% 或高于 90% 同样会触发 Daisy 检测。简言之，Daisy 认为，屏幕亮度不当和环境光不当都会对眼睛产生负面影响，然而改变这一状况，主要应从改变环境光入手；
3. **第三步：提醒指令（免费版和付费版都需要）**：打开快捷指令（Shortcuts），安装此快捷指令[Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924)，**请不要改动这一快捷指令中的内容，也不要改动其名称**。安装完此指令后可以实现基本功能；
4. **第四步：明暗指令（仅付费版）**：同上，打开快捷指令，然后安装太暗情况下的快捷指令[DarkTime-BrightnessUp](https://www.icloud.com/shortcuts/a44e83dc08c645298b239ae92eebff5a)，以及太亮情况下的快捷指令[BrightTime-BrightnessDown](https://www.icloud.com/shortcuts/4feeccf198544951b68b0da8acc8b2af)。这两个指令的内容结构有细微差别，都需要用户自定义修改。受限于快捷指令的功能，用户需要在每一个“Set Multiple accessories”的地方手动选择自己需要调整的设备，然后对应地调整其亮度。调整亮度的规则是：如果是 DarkTime-BrightnessUp 这个指令集，在每个 if 情况中，都将目标亮度设置为范围最大值加上 10% 的数字。例如，在“If Brightness is between 11 and 20”这个 if 命令中，设备的亮度应手动拖至 30%，这样就可将亮度在 11%-20% 之间的环境光设备调高 10%-20%，至 30%。相反，如果是 BrightTime-BrightnessDown 这个指令集，那么在每个 if 指令中，设备的亮度应该调整至范围最小值减去 10%（或 11%，根据情况）的数字。又如，在“f Brightness is between 21 and 30”命令中，设备的亮度应手动拖至 10%。效果刚好是相反的。如此，我们就实现了一个最多以 20% 为一阶的亮度调整组合。如果用户想实现更加细致的调整，也可以在此基础上增加更多 if 条件和命令，只是更复杂一点而已。在安装和自定义完此指令后，Daisy 的所有功能就都可以实现了。
5. **第五步：客制调整（仅付费版）**：如有修改 20-90 这一亮度区间的需求，Pro 用户可以在设置中手动更改这一数值，另外，**请务必记得前往[Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924)中更改对应的数值**。修改时请注意，在 Daisy 软件中使用的是整数，而在快捷指令中使用的是百分比小数。
6. **第六步：开始使用**：在设置完了以上内容后，选上 Switch on Daisy! 边上的小勾，即可开始使用！

## 使用说明

### 打开时
首次启动时，macOS 将弹出警告，因为 Daisy 不是通过 App Store 分发的软件，因此会有这样的警告，请同意。

<p align="center">
  <img src="https://i.imgur.com/nH5upbA.png" width=400 />
</p>

启动 Daisy，Mac 将弹出以下权限提醒，请选择 OK。

<p align="center">
  <img src="https://i.imgur.com/ROzbYpM.png" width=400 />
</p>

接着在任务栏里面访问 Daisy，点击图标，弹出下拉框，选择第一项“Switch on Daisy!”即可启动 Daisy。启动时第一栏前面会有一个小勾，如果需要临时取消，那么也可以再点击一下，当勾消失之后即停止 Daisy。

### 更新时

直接将新版本的 .app 文件拖入软件文件夹（Application）即可。

### 从免费版进阶为付费版时

同上，将付费版的 .app 文件拖入软件文件夹（Application）即可。

## 注意事项

1. 如果电脑合盖的话，一般来说，电脑会自动熄屏上锁，因此 Daisy 会检测到这一种情况，并停止检测——否则，解锁后会发现一大堆灯光提醒。但是**如果使用者个人设置合盖不熄屏的话**——很多人用第三方软件设置这个功能——那么 Daisy 肯定会一直检测环境光，而合盖后的环境光可能会非常差，因此会弹出很多提醒，如果关联了快捷指令，那么也可能会不断触发外部指令。因此，如果有类似的需求，**希望使用者在合盖之前停止 Daisy 的检测，在下次开始开盖后打开即可**。
2. 如果出现了下图所示的提示，表示 Daisy 没法通过 Shortcuts 指示 Home 中绑定的智能设备。但是不必担心，这时候**只需打开 Home 软件等待自动连接更新状态即可**，这可能是由于苹果 Home 连接上的一些问题。

<p align="center">
  <img src="https://i.imgur.com/i3rFp5l.png" width=400 />
</p>

3. 关于手动调节，即便开启了根据环境亮度调节亮度，MacBook 也会尊重你的手动调节，因此这里没有非此不可的正确答案，用户尽可以在打开根据亮度调节后，在当前自己认为眼睛最舒适的环境中确定一个亮度锚点，此后环境光亮度变化而引发的设备亮度变化都将围绕这个锚点上下波动。Daisy 也会根据这个值来执行自动指令。
4. 关于五阶的亮度，其实并非完全地每 20 度分一阶。建议的做法是在亮度升高和亮度降低两个指令集中错开 10 度。这样可以避免环境灯在固定的五阶上来回摆动，无法调至其他亮度。例如，若不错开地排布，那么亮度只会在 0、20、40、60、80 和 100 之间变化，自动指令就无法调至 50 度。而如果错开 10 度，那么亮度可以先从 40 升高至 60，然后再降至 50，可确保更多选项。
5. 如果在安装下载快捷指令时出现“Can't connect to the Gallery.”（无法连接到“快捷指令中心”）的字样，虽然很有可能是用户的网络和软件设置存在故障，但亦有可能是苹果服务器的问题。后者也曾经发生过，因此如遇此情况，只能等待苹果修复服务器连接才能继续。在这段时间内，如果用户着急想要获取快捷指令的内容，可以通过邮件或本页上部的各种联系方式和开发者取得联系，开发者可以发送快捷指令截图，辅助用户自行创建快捷指令。

## 证书信息

GPL-3.0 license

## 特别致谢

1. [Qt](https://github.com/qt)：本软件遵循 Qt 的开源协议。

## 支持作者

[Buy Me a Cup of Coffee](https://www.buymeacoffee.com/ryanthehito)

<p align="center">
  <img src="https://i.imgur.com/OHHJD4y.png" width=240 />
  <img src="https://i.imgur.com/6XiKMAK.png" width=240 />
</p>
