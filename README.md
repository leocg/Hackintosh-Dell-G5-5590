# Hackintosh-Dell-G5-5590

## :computer: ​Laptop Specs

### Dell G5 5590 A70P/M70P/A80P/M80P [RTX 2060 or GTX 1660 Ti models]

| Component      | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Processor      | Core i7-9750H 6C/12T (Coffee Lake Refresh)                   |
| iGPU           | Intel UHD 630 Graphics                                       |
| dGPU           | ~~nVidia GeForce RTX 2060~~  (not supported)                 |
| Display        | 15.6 1080p (1920x1080) 144hz                                 |
| Memory         | 16GB DDR4 2666MHz (8GBx2)                                    |
| Storage        | 512GB Intel NVMe SSD                                         |
| Audio          | Realtek ALC3204-CG (ALC236)                                  |
| Wifi/Bluetooth | ~~Qualcomm QCA61x4A (DW1820)~~ (wifi not supported / bluetooth supported, replaced with card described in next table) |
| Ethernet       | Killer GB E2500V2 10/100/1000 Mbps                           |

| Extra Hardware    | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| SSD in second bay | 1tb SSD (Crucial BX500)                                      |
| Wifi/Bluetooth    | Fenvi BCM94360NG (ordered m2 card at aliexpress from Fenvi Store) |



### Tested with: 

- ### macOS Catalina v10.15 (since initial release)

- ### macOS Big Sur v11 (since v2.0)

- ### macOS Monterey v12 (since v3.0) 

- ### macOS Ventura v13 (since v4.0)

![](https://raw.githubusercontent.com/leocg/Hackintosh-Dell-G5-5590/master/UTIL/SCREENSHOTS%20PROOFS/Geekbench%20October%202022%20macOS%2013.0.png)



## INSTALLATION

Tested with RTX 2060 and GTX 1660 Ti versions, both [share same hardware specs](https://topics-cdn.dell.com/pdf/g-series-15-5590-laptop_setup-guide_pt-br.pdf) (Thunderbolt 3 port)

### BIOS VERSION (Check your BIOS version before anything)

- 1.13.2
- 1.14.0
- 1.21.1 (Thanks to **[al-jabirr](https://github.com/al-jabirr)** for testing and pointing out)

Updating BIOS will reset CFG-Lock and Undervolting to factory settings, after update you must follow the steps to disable CFG-Lock and enable Undervolting again.

#### Read [official guide](https://dortania.github.io/OpenCore-Install-Guide/) to understand stuff, not needed, but it's nice to understand what you're doing

#### BIOS SETUP:

- General -> Advanced Boot Options -> Uncheck "Enable Legacy Options ROMs"
- General -> UEFI Boot Path Security -> Check "Never"
- System Configuration -> Integrated NIC -> Uncheck "Enable UEFI Network Stack". Check option "Enabled"
- System Configuration -> SATA Operation -> Check "AHCI"
- System Configuration -> SMART Reporting -> Check "Enable SMART Reporting"
- System Configuration -> USB Configuration -> Check "Enable USB Boot Support" and "Enable External USB Port"
- System Configuration -> Thunderbolt Adapter Configuration -> Check "Enable Thunderbolt Technology Support" and "Security Level - No Security"
- System Configuration -> Thunderbolt Auto Switch -> Uncheck "Auto Switch" and Check "BIOS Assist Enumeration"
- System Configuration -> USB Power Share -> Uncheck "Enable USB PowerShare"
- Security -> Computrace -> Check "Deactivate"
- Secure Boot -> Secure Boot Enable -> Uncheck "Secure Boot Enable"
- Intel Software Guard Extensions -> Intel SGX Enable -> Check "Disabled"
- Performance -> Intel Speedstep -> Check "Enable Intel SpeedStep"
- Performance -> C-States Control -> Check "C states"
- Performance -> Intel TurboBoost -> Check "Enable Intel TurboBoost"
- Performance -> HyperThread control -> Check "Enable"
- Power Management -> Enable Intel Speed Shift Technology -> Check "Enable Intel Speed Shift Technology"
- Power Management -> USB Wake Support -> Uncheck "Enable USB Wake Support"
- Virtualization Support -> Virtualization -> Check "Enable Intel Virtualization Technology"
- Virtualization Support -> VT for Direct I/O -> Uncheck "Enable VT for Direct IO"



#### OPENCORE SETUP:

- Download latest release from [Releases page](https://github.com/leocg/Hackintosh-Dell-G5-5590/releases)
- Choose the right EFI folder for you:
  - OpenCanopy AudioDxe: OpenCore with GUI partition picker and boot chime sound. I use this version.
  - OpenCanopy: OpenCore with GUI partition picker
  - Verbose: OpenCore with text only partition picker
- Open config.plist and make some changes:
  - If you want to enable verbose mode during installation, go to NVRAM->Add->7C436110-AB2A-4BBB-A880-FE41995C9F82, and insert **-v** on **boot-args**. To disable verbose mode, just remove -v parameter.
  - Generate your **MacBookPro15,2** serials using [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS/) and insert it into your config.plist (under PlatformInfo->Generic). You need to update MLB, SystemSerialNumber and SystemUUID. 
  - It's recommended to disable CFG Lock. CFG Lock prevents OS X from writing to a certain region in your BIOS. macOS does this for power management and other reasons, and if it can't access it, it will not boot. You can find instructions for disabling at **DISABLING CFG LOCK** section in this document. If you disabled it, don't change the lines below. In case you don't want to mess with it, you have to change 2 properties under Kernel->Quirks in order to boot macOS without disabling it:
    - AppleCpuPmCfgLock to **YES** or **1** 
    - AppleXcpmCfgLock to **YES** or **1**
  - After installation you can make the default OpenCore selection by pressing Ctrl+Enter on the partition you want in the OpenCore boot picker.
  - You can also disable OpenCore boot picker under Misc->Boot->ShowPicker (change to NO). Only do this if you keep an extra copy of OpenCore with boot picker enabled in a USB Drive in case you need to use the OpenCore interface.
  - **Remember to keep an USB copy of your EFI folder.** Normally I use one pen drive for tests, one pen drive with a working OpenCore version + macOS installer in case I need to do some recovery and stable version on my SSD EFI Folder.

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/master/UTIL/SCREENSHOTS%20PROOFS/DOCS/CFG%20Lock.png)



#### DISABLING CFG LOCK (optional):

The i7 9750h CPU supports disabling CFG Lock, but it's not disabled by default in BIOS. In order to disable, you'll need to follow some steps:

1. Format a USB drive to FAT32 on a GUID partition map.
2. Make a folder called EFI in the root of the USB
3. Inside this, make a folder called BOOT
4. Download [this](https://github.com/datasone/grub-mod-setup_var/releases/download/1.1/modGRUBShell.efi) file and place it inside BOOT
5. Rename this file to bootx64.efi
6. Boot into the USB drive (spam F12 at the BIOS prompt and select your USB drive)
7. Once this has loaded, enter **setup_var_3 0x5C4 0x00** to disable CFG lock. You can disable Undervolting lock now too, following step 7 from the **UNDERVOLTING** section.
8. Enter **reboot** to exit and restart your computer.
9. You can verify if your CFG Lock is disabled using ControlMsrE2.efi from OpenCore OC/Tools folder. Copy it to your EFI/OC/tools and put the parameters below into your config.plist at Misc -> Tools:

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/master/UTIL/SCREENSHOTS%20PROOFS/DOCS/ControlMsrE2.png)

10. Reboot your laptot and select ControlMsrE2 in the boot picker. If your CFG Lock is successfully disabled, you will see the information "This firmware has UNLOCKED MSR 0xE2 register!".

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/master/UTIL/SCREENSHOTS%20PROOFS/DOCS/CFG-Lock-Disabled-BIOS.png)

#### UNDERVOLTING (optional):

The i7 9750h CPU supports undervolting, but it's not enabled by default in BIOS. In order to enable, you'll need to follow some steps, pretty similar to disable CFG Lock:

1. Format a USB drive to FAT32 on a GUID partition map.
2. Make a folder called EFI in the root of the USB
3. Inside this, make a folder called BOOT
4. Download [this](https://github.com/datasone/grub-mod-setup_var/releases/download/1.1/modGRUBShell.efi) file and place it inside BOOT
5. Rename this file to bootx64.efi
6. Boot into the USB drive (spam F12 at the BIOS prompt and select your USB drive)
7. Once this has loaded, enter **setup_var_3 0x660 0x00** to disable overclocking lock. You can disable CFG Lock now too, following step 7 from the **DISABLING CFG LOCK** section.
8. Enter **reboot** to exit and restart your computer.

Now you have undervolting enabled. Next step: download VoltageShit (https://github.com/sicreative/VoltageShift) and extract it. I place the voltageshift folder inside Applications folder.

Next make some tests in order to define the best frequency for you. I got a very stable setup using -225mv CPU voltage offset ans -125mv on CPU Cache voltage offset. Start with -125mv in both and then try to rise CPU voltage offset to -225mv:

- Go to VoltageShift folder using terminal, in my case: `cd /Applications/voltageshift`
- Set the desired offset, example: `./voltageshift offset -125 0 -125` (first value is CPU, second value is GPU and third value is CPU Cache). You can try other values for best stability, starting with lower values and going up. If you set to high your laptop may freeze. In this case, hard restart and try again with lower values. Ideally you shoud start with `./voltageshift offset -25 0 -25` and step up 25mv each time. CPU voltage offset can be more than CPU cache offset. I read in a forum people getting good results with -225mv CPU and -125mv CPU cache. I got good results with it too and I'm using it for about a month without issues (I run -125mv CPU and -125mv CPU cache for a couple of months without issues too).
- After you test throughfuly the settings and are comfortable with System stability, you can apply the launchd in order to set undervolt on boot: `./voltageshift buildlaunchd -225 0 -125` (remember to set the CPU and CPU cache values with your desired values)
- There's some other parameters you can include on buildlaunchd, like run the utility every X minutes if your system is disabling undervolting after sleep, for example. I'm only running on boot and didn't have any issues so far. Read more at https://github.com/sicreative/VoltageShift 

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/e4dd84265ea434a8f0049d8c65d94ba044548a93/UTIL/SCREENSHOTS%20PROOFS/VoltageShift.png)

#### Updating OpenCore:

When a new release is avaliable, just download the zip file and update the new config.plist with your old config.plist values:

**PlatformInfo -> Generic**

- MLB
- SystemProductName
- SystemSerialNumber
- SystemUUID

If you didn't disable CFG LOCK, change the values below (**don't need to change if you disabled CFG LOCK**):

**Kernel -> Quirks**

- AppleCpuPmCfgLock (change the value to 0 or NO, depending on the syntax of your editor. If it's 1 change to 0. If it's YES change to NO)
- AppleXcpmCfgLock (change the value to 0 or NO, depending on the syntax of your editor. If it's 1 change to 0. If it's YES change to NO)



## KNOWN ISSUES

- Some DRM videos won't work. Currently you can view videos encoded with **FairPlay 2.x/3.x**.
- External mic not working (only work with bluetooth headset). Already tried to use ComboJack and tested all layout IDs avaliable for ALC236 without success. If you want to dig into this issue, you can read about creating a custom codec at [AppleALC Wiki](https://github.com/acidanthera/AppleALC/wiki/Adding-codec-support). You can also try to add custom codec into [this version of ComboJack](https://github.com/lvs1974/ComboJack) (see Add your codec topic). 
- Sometimes unplugging/replugging quickly causes laptop to crash. To avoid this issue, put laptop to sleep before plug or unplug the power chord. I'm revisiting all ACPI settings, but no luck so far.   *Update: I found the cause. It's related to turning off dGPU. Leaving dGPU enabled, the issue is gone. Activating it with any method (-wegnogpu boot flag, optimus method, device method in config.plist, etc) will cause the freeze. I'm leaving dGPU disabled because battery life goes down to 30 minutes with it enabled, but you can disable it removing SSDT-dGPU-Off.aml from ACPI in config.plist. I'm looking for solutions to disable dGPU without freezing after unplug. 



## WORKING

:white_check_mark: iGPU Acceleration    
:white_check_mark: Native brightness control (Thanks [@caiomascarin](https://github.com/caiomascarin))   
:white_check_mark: 144hz display   
:white_check_mark: External monitor using USB-C to HDMI adapter. Other ports (HDMI and Mini Display Port) won't work, they're liked to nVidia GPU   
:white_check_mark: Apple Services  
:white_check_mark: Keyboard with backlight (RGB backlight works, but had to setup at Windows 10 Alienware Command Center. When boot at macOS the config remains, including color. I'm able to work with Alienware Command Center using VMware Fusion to boot Windows 10 partition (as Boot Camp) and connecting Alienware AW-ALC in Virtual Machine -> USB & Bluetooth. Had to reboot a few times in order to work for the first time.  
:white_check_mark: Trackpad with multitouch gestures  
:white_check_mark: Speakers  
:white_check_mark: Microphone  
:white_check_mark: Webcam  
:white_check_mark: USB 2/3/C ports   
:white_check_mark: Card reader  
:white_check_mark: CFG Lock disabled  
:white_check_mark: [NVRAM](https://dortania.github.io/OpenCore-Post-Install/misc/nvram.html#verifying-if-you-have-working-nvram)  
:white_check_mark: Bluetooth - Using Fenvi BCM94360NG (Original card worked with bluetooth out of box too)  
:white_check_mark: USB-C video out  (using generic USB-C to HDMI adapter)  
:white_check_mark: Ethernet (Thanks [@radaelilucca](https://github.com/radaelilucca))  
:white_check_mark: FairPlay 2.x/3.x DRM videos
:white_check_mark: :warning: Apple Communications (Continuity, airdrop, etc) - Using Fenvi BCM94360NG (Original card didn't provide support)  
:white_check_mark: :warning: Wi-Fi - Using Fenvi BCM94360NG (Original card don't work on macOS)    
:white_check_mark: :warning: Thunderbolt 3 (can see device in Hackintosh but don't have any Thunderbolt peripheral to test)

## NOT WORKING

:x: nVidia GPU - not compatible with macOS

:x: HDMI and Mini Display Port video out (linked to nVidia GPU. Use USB-C to HDMI adapter to use external display)

:x: WiFi Qualcomm QCA61x4A (DW1820) - not compatible with macOS. Replaced mine with Fenvi BCM94360NG

:x: FairPlay 1.x and FairPlay 4.x DRM videos

:x: ComboJack (microphone). Headphone work fine, but mic don't work. You'll have to rely on the internal mic or bluetooth headset.



### SCREENSHOTS

#### AirDrop

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/e4dd84265ea434a8f0049d8c65d94ba044548a93/UTIL/SCREENSHOTS%20PROOFS/AIRDROP.png)



#### Continuity

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/e4dd84265ea434a8f0049d8c65d94ba044548a93/UTIL/SCREENSHOTS%20PROOFS/Continuity.png)



#### Video Acceleration

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/e4dd84265ea434a8f0049d8c65d94ba044548a93/UTIL/SCREENSHOTS%20PROOFS/HVEC%20Encoding%20Support.png)



#### iMessage

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/master/UTIL/SCREENSHOTS%20PROOFS/iMessage%20Working.png)



#### NMVe Disk Speed Test

![](https://github.com/leocg/Hackintosh-Dell-G5-5590/raw/e4dd84265ea434a8f0049d8c65d94ba044548a93/UTIL/SCREENSHOTS%20PROOFS/NVMe%20DISK%20Speed%20Test.png)



If you like this guide and want to help with any value, please buy me a coffee :coffee:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=N7EY58HHR9RUQ)



## CHANGELOG



**JANUARY 24 2023** 

- Updated to macOS Ventura 13.2 using software updater without issues with OpenCore 0.8.5.

**JANUARY 13 2023** 

- Updated to macOS Ventura 13.1 using software updater without issues with OpenCore 0.8.5.

**DECEMBER 06 2022** 

- Updated to macOS Ventura 13.0.1 using software updater without issues with OpenCore 0.8.5.

**OCTOBER 24 2022** (v4.0)

- Updated to OpenCore 0.8.5 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2022/10/04/acidanthera-october.html).
- Updated to macOS Ventura 13.0 using software updater without issues with OpenCore 0.8.5.

**AUGUST 23 2022** (v3.4)

- Updated to OpenCore 0.8.3 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2022/08/02/acidanthera-dortania-august.html).
- Updated to macOS Monterey 12.5.1 using software updater without issues with OpenCore 0.8.3.

**View past updates on [Changelog.md](https://github.com/leocg/Hackintosh-Dell-G5-5590/blob/master/Changelog.md)**



## About

This is my "Hackintosh Diary", will be using it to maintain a triple boot Dell G5 5590 a80p between macOS, Arch Linux and Windows.  

Used [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) from [Dortania](https://dortania.github.io/), but laptop and desktop guide was merged into [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/).
