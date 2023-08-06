# 🌼Daisy: Ambient Light Reminder and Auto-switcher

![65ldrAT](https://i.imgur.com/65ldrAT.png)

<p align="center">English | <a href="README_cn.md">简体中文</a></p>

<p align="center"><a href="https://t.me/+AODLypeF_aYwYjNh">Telegram</a> | <a href="https://twitter.com/ryanswindows">Twitter</a> | <a href="https://weibo.com/ryanthehitos">Weibo</a></p>

Daisy is an app for macOS that alerts the user that the ambient light is too bright or too dim, and (in the Pro version) automatically adjusts the ambient brightness for eye protection.

## Problems to Solve

Eye protection is a pressing concern for individuals who spend extended periods of time in front of computer screens. In addition to features like Night Shift and True Tone, third-party software can also monitor eye time and adjust color temperature, brightness and theme. **However, I believe that the primary focus of eye protection should be on managing eye time and optimizing ambient light brightness rather than solely focusing on themes or color temperatures.** Are theme and color temperature not favorable? Not necessarily. Regarding color temperature, there are screen films with filtration functions that can achieve 24-hour hardware-level filtration, making software adjustments less necessary. Another factor to consider is that color temperature affects display accuracy, which poses challenges for those who engage in photography and retouching regularly. I believe that the original intention of light and dark themes may not be for eye protection. The dark theme, which features a dark background with white characters, does make the text on the screen appear clearer. However, constantly looking at the screen can cause eye fatigue. Increased clarity can also strain the eyes further. To achieve a balance between our needs and eye protection, it is important to limit the amount of time spent using our eyes and ensure that the ambient light is neither too dark nor too bright. Since there are no software products available for now, I plan to create one.

Another motive is that there are already some mature third-party noise detection software on Mac, which can prompt users whether they are exposed to a noisy environment. I have previously written a software called [Cherry](https://github.com/Ryan-the-hito/Cherry) to adjust the system volume changes to prevent the sound from being too loud or too low. Although there are products that focus on sound management for the environment and the system, there are rarely tools specifically designed for light management. [f.lux](https://justgetflux.com/) does have ambient light management, but it adjusts the warmth of the ambient light rather than the brightness. I hope this product can learn from the strengths of reminder tools and also enhance the application of light management.

## Functions

###  Ambient Brightness Reminder (basic function)：

Just like all reminder tools, Daisy's primary function is to remind users when the ambient light is too dim or too bright. Mac has ambient light sensors on many models. However, Daisy does not obtain ambient light brightness through the native method. Instead, it operates alongside other software and system functions. Usually macOS has a built-in feature to automatically adjust screen brightness based on ambient light, so users can firstly enable "Automatically adjust brightness". However, this system function does not include a reminder feature like Daisy does. Therefore, Daisy defines "too dim" as 20% screen brightness and "too bright" as 90%. If the screen brightness, which changes with ambient light, falls below 20% or exceeds 90%, Daisy will be triggered to remind users to adjust ambient light according to the current situation.

### Automatic Adjustment of Ambient Light (Pro feature)：

If the user has smart devices, such as a smart desk lamp for lighting, they can connect it to Home. Daisy can also issue commands through Shortcuts to adjust the brightness of this smart device: when the ambient light is dim, increase the brightness of the device by 10%-20%, and vice versa.

## Interface

<p align="center">
  <img src="https://i.imgur.com/1Huutz9.png" width=400 />
</p>

Daisy does not have a main interface, only a settings interface. In this interface, the first line allows you to set how often Daisy should check for updates. By default, this is set to occur every 30 seconds. This feature is included in both the free and Pro versions as a basic function.

The second and third settings are only available in the Pro version. The second setting allows you to customize the brightness range by determining a critical value. The third setting is optional, allowing users to choose whether or not to enable shortcuts for specific situations. If enabled, Daisy will execute the corresponding shortcut based on the situation. Users should write the names of their desired shortcuts in the column next to each situation. By default, "DarkTime-BrightnessUp" is assigned as the shortcut for dark scenes and "BrightTime-BrightnessDown" is assigned for bright scenes. Remember to click Save after modifying these settings. The mentioned shortcuts can be found in the default templates provided below.

Reminder interface:

<p align="center">
  <img src="https://i.imgur.com/8CrVApk.png" width=400 />
</p>

If automatic adjustment is enabled, Daisy will not only remind you of the brightness but also give reminders before and after adjusting the ambient light:

<p align="center">
  <img src="https://i.imgur.com/KThHm7N.png" width=400 />
</p>

After running on my computer for about 24 hours, the power consumption is very low:

<p align="center">
  <img src="https://i.imgur.com/6OsBRWb.png" width=400 />
</p>

The "Settings" section of the free version and Pro version:

<p align="center">
  <img src="https://i.imgur.com/hiy7G6L.png" width=400 />
  <img src="https://i.imgur.com/1Huutz9.png" width=400 />
</p>

The "About" section of the free version and Pro version:

<p align="center">
  <img src="https://i.imgur.com/p39Zcwd.png" width=400 />
  <img src="https://i.imgur.com/36aBGkT.png" width=400 />
</p>

## DEMO

https://github.com/Ryan-the-hito/Daisy/assets/95213517/e44db030-bf11-4b85-bd54-a44f867e5f2e

## Environment Requirements

- MacOS 12 Monterey or above (test environment is MacOS 12.6.5)
- M1, M2 chips
- Network environment (for installing shortcuts)

## Pricing

|      | Free                      | Pro                      |
|------|-----------------------------|-----------------------------|
| Basic functions |1. Remind if the ambient light is too dark or too bright<br>2. Set the intervals for automatically detecting the ambient light. | 1. Remind if the ambient light is too dark or too bright<br>2. Set the intervals for automatically detecting the ambient light.|
| Pro features | None | 3. Customize the brightness range for too dark and too bright.<br>4. Automatically execute shortcuts when it is too dark or too bright and adjust the brightness of smart lights in Home.|
| Price | Free                        | $1（Only for 1 buck）      |
| Get | [Github Releases](https://github.com/Ryan-the-hito/Daisy/releases)<br>[Google Drive](https://drive.google.com/drive/folders/1sqAwRH-3suDPkl_GV78qW_-BklWU20Ru?usp=drive_link)<br>[Baidu Netdisk](https://pan.baidu.com/s/1dW27Pi_Fi-BhyZTMTzBzag?pwd=75q3)<br>[Dropbox](https://www.dropbox.com/scl/fo/nrn30qjqffsebrzlkxilv/h?rlkey=09vmwun931k3ugw0j1qd8njpa&dl=0)  | [Click to buy](https://www.buymeacoffee.com/ryanthehito/e/155171) |

## Installation

1. **Step 1: Download the software**: Download the compressed file, unzip it and drag it to the software folder (Application).
2. **Step 2: Setting up detection**: Open system settings (System Preferences or System Settings), go to the Display section, and check the option for "Automatically adjust brightness" as shown in the following image:
   <p align="center">
	<img src="https://i.imgur.com/TPa11q3.png" width=400 />
	</p>
   打开之后，电脑屏幕的亮度就会自动地由系统管理，因此不建议手动调整电脑屏幕，而是通过调整环境光的角度和亮度来实现良好的办公环境。许多用户因为自动亮度太低而是手动拉高屏幕亮度值，但是这恰恰是伤眼的——这说明用户此时身处一个环境光较暗的空间，但是相反却使用较高亮度的屏幕，对眼睛的压力会更大。除非特殊情况，否则将屏幕亮度调至低于 20% 或高于 90% 同样会触发 Daisy 检测。简言之，Daisy 认为，屏幕亮度不当和环境光不当都会对眼睛产生负面影响，然而改变这一状况，主要应从改变环境光入手；
3. **第三步：提醒指令（免费版和付费版都需要）**：打开快捷指令（Shortcuts），安装此快捷指令[Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924)，**请不要改动这一快捷指令中的内容，也不要改动其名称**。安装完此指令后可以实现基本功能；
4. **第四步：明暗指令（仅付费版）**：同上，打开快捷指令，然后安装太暗情况下的快捷指令[DarkTime-BrightnessUp](https://www.icloud.com/shortcuts/a44e83dc08c645298b239ae92eebff5a)，以及太亮情况下的快捷指令[BrightTime-BrightnessDown](https://www.icloud.com/shortcuts/4feeccf198544951b68b0da8acc8b2af)。这两个指令的内容结构有细微差别，都需要用户自定义修改。受限于快捷指令的功能，用户需要在每一个“Set Multiple accessories”的地方手动选择自己需要调整的设备，然后对应地调整其亮度。调整亮度的规则是：如果是 DarkTime-BrightnessUp 这个指令集，在每个 if 情况中，都将目标亮度设置为范围最大值加上 10% 的数字。例如，在“If Brightness is between 11 and 20”这个 if 命令中，设备的亮度应手动拖至 30%，这样就可将亮度在 11%-20% 之间的环境光设备调高 10%-20%，至 30%。相反，如果是 BrightTime-BrightnessDown 这个指令集，那么在每个 if 指令中，设备的亮度应该调整至范围最小值减去 10%（或 11%，根据情况）的数字。又如，在“f Brightness is between 21 and 30”命令中，设备的亮度应手动拖至 10%。效果刚好是相反的。如此，我们就实现了一个最多以 20% 为一阶的亮度调整组合。如果用户想实现更加细致的调整，也可以在此基础上增加更多 if 条件和命令，只是更复杂一点而已。在安装和自定义完此指令后，Daisy 的所有功能就都可以实现了。
5. **第五步：客制调整（仅付费版）**：如有修改 20-90 这一亮度区间的需求，Pro 用户可以在设置中手动更改这一数值，另外，**请务必记得前往[Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924)中更改对应的数值**。修改时请注意，在 Daisy 软件中使用的是整数，而在快捷指令中使用的是百分比小数。
6. **第六步：开始使用**：在设置完了以上内容后，选上 Switch on Daisy! 边上的小勾，即可开始使用！

## Instructions for use

### When opening

When it starts for the first time, macOS will pop up a warning, because Daisy is not the software distributed through the App Store, so there will be such a warning. Please agree.

<p align="center">
  <img src="https://i.imgur.com/nH5upbA.png" width=400 />
</p>

Start Daisy, Mac will pop up the following permission prompt, please select OK.

<p align="center">
  <img src="https://i.imgur.com/ROzbYpM.png" width=400 />
</p>

Next, access Daisy in the taskbar, click on the icon, and a dropdown menu will appear. Select the first option "Switch on Daisy!" to start Daisy. There will be a small checkmark in front of the first column when it is launched. If you need to temporarily cancel it, you can also click again. Once the checkmark disappears, Daisy will stop running.

### When updating

Simply drag the new version's .app file into the software folder (Application).

### When upgrading from the free version to the Pro version

Same as above, just drag the Pro version's .app file into the software folder (Application).

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
