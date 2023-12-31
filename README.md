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


Purchase and Payment Instructions:

To purchase this software, please follow the instructions below:

1. Visit the (Buy me a coffee link)[https://www.buymeacoffee.com/ryanthehito/e/155171].
2. Fill in your name and email address in the provided fields.
3. Choose your preferred payment method: bank card or link.
4. Complete the payment process.
5. Upon successful payment, you will receive the Pro version software package.
6. The software package can be installed on multiple devices.

Thank you for your support and recognition of open-source paid software. As an independent developer, I deeply appreciate the encouragement from all supporters.

<p align="center">
  <img src="https://i.imgur.com/cMrTPxi.png" width=400 />
  <img src="https://i.imgur.com/xdsznlL.png" width=400 />
</p>

## Installation

1. **Step 1: Download the software**: Download the compressed file, unzip it and drag it to the software folder (Application).
2. **Step 2: Setting up detection**: Open system settings (System Preferences or System Settings), go to the Display section, and check the option for "Automatically adjust brightness" as shown in the following image:
   <p align="center">
	<img src="https://i.imgur.com/TPa11q3.png" width=400 />
	</p>
   Then the brightness of screen will be automatically managed by the system, so it is not recommended to adjust the computer screen manually. Instead, a good working environment can be achieved by adjusting the angle and brightness of the ambient light. Many users increase the screen brightness manually because they find the automatic brightness too low, but this strains the eyes. This always indicates that the user is in a dimly lit space but using a high brightness screen, which puts more pressure on the eyes. Unless in special circumstances, adjusting the screen brightness below 20% or above 90% will trigger Daisy's detection. In short, Daisy believes that improper screen brightness and improper ambient light have negative effects on the eyes. To address this issue, focus should primarily be on changing the ambient light conditions.
3. **Step 3: Reminder command (both free and paid versions)**: Open Shortcuts and install the shortcut command [Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924). **Please do not modify the content in this shortcut command, nor modify its name**. After installing this command, the basic functions can be realized;
4. **Step 4: Brightness commands (Pro version only)**: Same as above, open Shortcuts, and then install the shortcut [DarkTime-BrightnessUp](https://www.icloud.com/shortcuts/a44e83dc08c645298b239ae92eebff5a) for dark situations, as well as the shortcut [BrightTime-BrightnessDown](https://www.icloud.com/shortcuts/4feeccf198544951b68b0da8acc8b2af) for bright situations. The content structure of these two shortcuts is slightly different and needs to be customized by the user. Due to the limitations of Shortcuts, users need to manually select the devices they want to adjust in each "Set Multiple accessories" section, and then adjust their brightness accordingly. The rule for adjusting brightness is as follows: If the shortcut is DarkTime-BrightnessUp, set the target brightness to 10% above the maximum range in each "if" condition. For example, in the "If Brightness is between 11 and 20" command, manually adjust the device's brightness to 30%. This will increase the brightness of the ambient light device between 11% and 20% by 10% to 19%, up to 30%. If it is the BrightTime-BrightnessDown shortcut, adjust the device's brightness to 11% below the minimum range in each "if" command. For example, in the "If Brightness is between 21 and 30" command, manually adjust the device's brightness to 10%. The effect is just the opposite. In this way, we have achieved a brightness adjustment combination with a maximum of 20% for each step. If users want to achieve more detailed adjustments, they can add more "if" conditions and commands on this basis, but it will be a bit more complicated. After installing and customizing this shortcut, all of Daisy's functions can be achieved
5. **Step 5: Custom adjustment (Pro version only)**: If there is a need to modify the brightness range of 20-90, Pro users can manually change this value in the settings. Additionally, **please remember to go to [Brightness Alarm](https://www.icloud.com/shortcuts/a5b22d5cbba741b7ba15e837106a3924) to change the corresponding value**. When making modifications, please note that integers are used in Daisy, while decimal percentages are used in the Shortcuts.
6. **Step 6: Start using**: After setting up the above details, tick the small box next to "Switch on Daisy!" to start using!

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

## Q&A

If there are any special circumstances, please visit **[Q&A](https://github.com/Ryan-the-hito/Q-A)❓** to see if there are ready-made solutions or contact me for further assistance.

## Notice

1. This software has no Chinese interface and solemnly declares that it does not engage in Internet information services within the territory of the People's Republic of China, not in the past, nor at present, and never in the future. All publicity, explanations, and payment channels of this software comply with the laws and regulations of the country and platform it is in. 
2. Generally, when the computer is closed, it will automatically turn off and lock the screen. Daisy detects this and stops detecting light to avoid unnecessary reminders upon unlocking. **However, if the user has manually disabled the screen turning off feature using third-party software**, Daisy will continue to detect ambient light even when the lid is closed. This may result in multiple reminders due to poor lighting conditions. Additionally, if there are associated shortcut commands, external instructions may be triggered repeatedly. **Therefore, if you have a similar requirement, please remember to disable Daisy's detection before closing the lid and enable it again afterwards**.
3. If you see the alert shown in the figure below, it means that Daisy is unable to control the smart devices linked to Home through Shortcuts. There's no need to worry, **simply open the Home app and wait for the automatic connection update**. This issue may be caused by a problem with the connection to Apple Home.

<p align="center">
  <img src="https://i.imgur.com/i3rFp5l.png" width=400 />
</p>

3. Regarding manual adjustment, even if the brightness is adjusted according to the ambient light when enabled, MacBook will still respect your manual adjustments. Therefore, there is no definitive correct answer here. Users can determine a brightness anchor point in their current environment that they find most comfortable for their eyes after enabling brightness adjustment based on ambient light. Subsequent changes in device brightness due to variations in ambient light will fluctuate around this anchor point. Daisy will also execute automatic commands based on this value. Even if the MacBook adjusts the brightness based on ambient light, it will still honor your manual adjustments. Therefore, there is no definitive correct answer. After enabling brightness adjustment based on ambient light, users can determine a comfortable anchor point for their eyes in their current environment. Changes in device brightness due to variations in ambient light will then fluctuate around this anchor point. Daisy will also execute automatic commands based on this value.
4. To improve the brightness control, it is recommended to stagger the intervals by 10 degrees between increasing and decreasing instructions. This will prevent abrupt changes in light levels and allow for more flexibility in adjusting brightness. For instance, without staggering, the brightness can only be set at fixed intervals of 0, 20, 40, 60, 80, and 100 degrees. As a result, automatic instructions cannot be adjusted to intermediate levels like 50 degrees. However, by staggering the intervals by 10 degrees, it becomes possible to increase from 40 to 60 and then decrease to precisely adjust to a desired level such as 50 degrees.
5. If you see the message "Can't connect to the Gallery." while installing or downloading shortcuts, it is likely due to network and software settings issues on your end. However, there is also a possibility that it could be a problem with Apple's server, which has occurred in the past. If this situation arises, we will need to wait for Apple to fix the server connection before proceeding. In the meantime, if you are eager to obtain the content of the shortcuts, please feel free to contact the developer through email or other contact methods provided at the top of this page. The developer can send screenshots of the shortcuts to assist you in creating them on your own.

## License

GPL-3.0 license

## Credit

1. [Qt](https://github.com/qt)：This software follows the open-source license of Qt.

## Sponsor me

[Buy Me a Cup of Coffee](https://www.buymeacoffee.com/ryanthehito)

<p align="center">
  <img src="https://i.imgur.com/OHHJD4y.png" width=240 />
  <img src="https://i.imgur.com/6XiKMAK.png" width=240 />
</p>

## Notifications

### 2023-11-07 The new update and BetterTouchTool functions

Hey! The Daisy pro version has been updated to v1.0.2 last week. And I would like to tell all of the Daisy users that now Daisy has fixed the issue of being killed by macOS in the background. Still, I have made Daisy look better in its update panel, which now offers dynamic check for latest releases. Any recommendation and comment would be favored in the Telegram group and via E-mails.

As for other apps with similar functions, I have noticed that BetterTouchTool has made some related functions to ambient light check and detection. In the latest release, you can see this function described as below.

![BTT](https://i.imgur.com/KezKnON.png)

And within the setting panel, you will find such functions. If you attach some Shortcuts to control your light bulbs (with Home support), it will be like the same as Daisy.

<p align="center">
  <img src="https://i.imgur.com/LCnVjwj.png" width=300 />
  <img src="https://i.imgur.com/byYEI9C.png" width=300 />
</p>

So is Daisy still necessary? I think so. And I have found some points that makes Daisy different. 

**First,** Daisy may be the first to detect ambient light and give you notifications. Well, it’s not a new comer~

**And second,** Daisy detects not only your ambient light, but also your screen light, or to make it easy, Daisy get data via your auto-changed screen light. Why not just use the sensor? The data from sensor would change dramatically and will easily trigger actions, which would easily resulted in false actions. Screen light will always be adjusted to the level that most people feel comfortable with, so if this level itself is too high or too low, it makes sense to notify you that you should pay more attention to your environment.

**Third,** as you can see from the setting panel, BetterTouchTool set the threshold using an absolute value, assuming the ambient light now is valued 1 (which is the absolute value related to the current value). This is typically difficult in determining how much value should I use when it is too dark or too bright. As the developer, I have tried using some data from the sensor, and it were all in digits, which is way too difficult for users. Daisy uses percentage, and 100% is always the brightest of your screen. I think this would be the easiest way to understand.

**Fourth,** BetterTouchTool introduced this function in such logic: Ambient light changes → Your Mac sleeps. The trigger is light and the action is to set your Mac. But Daisy comes in another way. Ambient light changes → Mac notifications → Light bulbs get brighter → Ambient light changes. Daisy’s focus has always been on the outside environment, rather within your Mac. Thus, Daisy is an app aiming at protecting your eyes.

**Fifth,** if you are going to control your bulb, both BetterTouchTool and Daisy will rely on Shortcuts. Just like how you use BetterTouchTool to assign different tasks in every scenario, you can do it with Daisy too by adding actions in certain Shortcuts script. Thus you would have more actions to be done, and it is as flexible as BetterTouchTool.

I hope that you may get a better understanding of Daisy’s positioning after reading the explanations above. I love BetterTouchTool too but it differs from Daisy in several ways. I also hope you will have a good time using both tools to make your life better.🥰