# Hackintosh-Dell-G5-5590

## Laptop Specs

### Dell G5 5590 a80p 

Processor: Core i7-9750H 6C/12T (Coffee Lake Plus / Coffee Lake Refresh) 
iGPU: Intel UHD 630 Graphics (Video Out using a **USB Type-C to DisplayPort adapter** into the USB 3.1 Gen 2 Type-C/DisplayPort 1.2/Thunderbolt 3 port)  
~~dGPU: nVidia GeForce RTX 2060~~ ~~(HDMI 2.0b port /mini DisplayPort 1.4)~~  
Display: 15.6 1080p (1920x1080) 144hz  
Memory: 16GB DDR4 2666MHz (8GBx2)  
Storage: 512GB Intel NVMe SSD + 1tb SSD (Crucial BX500)  
Audio: Realtek ALC3204-CG with support for nahimic  
Wifi/Bluetooth: Intel 9560 2x2 ac (80 MHz) (Wi-Fi 5 / Blueooth 5)  
Ethernet: Killer GB E2500V2 10/100/1000 Mbps  
USB 3.1  
Thunderbolt    
Webcam + Microphone  

## About

This is my "Hackintosh Diary", will be using it to maintain a triple boot Dell G5 5590 a80p between macOS, Arch Linux and Windows.  

Using [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) from [Dortania](https://dortania.github.io/)

## INSTALLATION

- [ ] Upgrade Windows 10 from Home to Pro
- [ ] Create Windows 10 recovery media: follow [this](https://www.dell.com/support/article/pt-br/sln297924/create-windows-10-recovery-media-for-your-dell-computer?lang=en) and [Imagem de recuperação Dell para Windows](https://www.dell.com/support/home/pt-br/drivers/osiso/WT64A)
- [ ] Partition NVME Disk Windows [220gb] macOS [220gb] Linux [70gb]: follow [1 Disk + Winders/Loonix](https://hackintosh-multiboot.gitbook.io/hackintosh-multiboot/uefi/1-disk-+-winders-loonix) **OR** choose easier path [2 Disks: Windows + Data + macOS](https://hackintosh-multiboot.gitbook.io/hackintosh-multiboot/uefi/2-disks-windows-+-data-+-macos)
- [ ] Install Arch Linux: follow [this](https://publications.petrzemek.net/articles/Dell-G5-15-Gaming-5590-Arch-Linux/)
- [ ] Use [rEFInd](http://www.rodsbooks.com/refind/) to manage bootloader. Install [Minimalistic black rEFInd theme](https://github.com/andersfischernielsen/rEFInd-minimal-black) OR view [this guide](https://dortania.github.io/OpenCore-Desktop-Guide/extras/gui.html) and try to setup OpenCore with GUI
- [ ] Follow [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) 
- [x] Generate OpenCore Catalina 10.5.5 USB Installation
- [ ] [An iDiot's Guide To Lilu and its Plug-ins](An iDiot's Guide To Lilu and its Plug-ins)
- [ ] Setup config.plist using [Coffee Lake Plus](https://dortania.github.io/vanilla-laptop-guide/OpenCore/config-laptop.plist/coffee-lake-plus.html)
- [ ] Copy EFI files to USB using [MountEFI](https://github.com/corpnewt/MountEFI). Maybe need to compile [SSDT-XOSI](https://github.com/hackintosh-guides/vanilla-laptop-guide/tree/master/Misc-files/SSDT-XOSI.aml) instead of SSDT-GPI0 and/or **[SSDT-PMC](https://dortania.github.io/Getting-Started-With-ACPI/)** if things go wrong.
  - [ ] **RebuildAppleMemoryMap** -> If panic, set to FALSE (Generates Memory Map compatible with macOS, can break on some laptop OEM firmwares so if you receive early boot failures disable this)
  - [ ] PciRoot(0x0)/Pci(0x2,0x0) (didn't mess with whatevergreen in first iteration)
  - [ ] **CustomSMBIOSGuid** if panic, set to YES, cause of relevance: Performs GUID patching for UpdateSMBIOSMode Custom mode. Usually relevant for Dell laptops
  - [ ] **BootProtect** set to Bootstrap, search for the fix
  - [ ] MacBookPro16,1 SMBIOS
  - [ ] **UpdateSMBIOSMode** Replace the tables with newly allocated EfiReservedMemoryType, use Custom on Dell laptops requiring CustomSMBIOSGuid quirk
- [ ] Remember to put -wegnoegpu NVRAM variable. Disable with [this](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/laptop-disable.html) method post installation.
- [ ] Remember to put alcid=xxx NVRAM variable. Will be fixing [post install](https://dortania.github.io/vanilla-laptop-guide/post-install/)
- [ ] Trackpad debug: follow [this](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/trackpad-methods/manual.html)
- [ ] Backlight debug: follow [this](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/backlight-methods/manual.html)
- [ ] Wi-Fi Intel 9560 alpha driver: follow [this comment](https://github.com/daliansky/XiaoMi-Pro-Hackintosh/issues/330#issuecomment-617738928)
- [ ] Share Bluetooth pairing between windows and mac: follow [this](https://www.reddit.com/r/hackintosh/comments/hjwu43/howto_share_a_bluetooth_pairing_headphones_etc/)
- [ ] Thunderbolt 3 Video out fix: follow [this](https://www.tonymacx86.com/threads/dell-g5-5590-thunderbolt-display-need-help.293776/)

## WORKING / NOT WORKING

- [ ] iGPU Acceleration 
- [ ] Backlight 
- [ ] 144hz display 
- [ ] Thunderbolt 3 video out 
- [ ] Ethernet
- [ ] Bluetooth
- [ ] Wi-Fi
- [ ] Apple Services
- [ ] Keyboard
- [ ] Keyboard backlight
- [ ] Trackpad
- [ ] Audio
- [ ] Microphone
- [ ] Webcam
- [ ] USB3 ports 
- [ ] Card reader

## TOOLS

- [OpenCore 0.5.9](https://github.com/acidanthera/OpenCorePkg)
- [gibMacOS](https://github.com/corpnewt/gibMacOS) - Download macOS vanilla install
- [MountEFI](https://github.com/corpnewt/MountEFI) - Mount EFI partitions
- [ProperTree](https://github.com/corpnewt/ProperTree) - Generate config.plist based on OC folder
- [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) - Generate Mac serials

## File History

**07 07 2020**

### Recovery operating system 

- macOS Catalina 10.5.5 (full install)

### KEXTs

- AppleALC.kext ([1.5.0](https://github.com/acidanthera/AppleALC/releases))
- Lilu.kext ([1.4.5](https://github.com/acidanthera/Lilu/releases))
- NoTouchID.kext ([1.0.3](https://github.com/al3xtjames/NoTouchID/releases))
- VirtualSMC.kext ([1.1.4](https://github.com/acidanthera/virtualsmc/releases))
  - SMCBatteryManager.kext (1.0)
  - SMCLightSensor.kext (1.0)
  - SMCProcessor.kext (1.1.4)
  - SMCSuperIO.kext (1.1.4)
- VoodooI2C.kext ([2.4.3](https://github.com/VoodooI2C/VoodooI2C/releases))
  - VoodooI2CHID.kext (1.0)
- VoodooPS2Controller.kext ([2.1.5](https://github.com/acidanthera/VoodooPS2/releases))
- WhateverGreen.kext ([1.4.0](https://github.com/acidanthera/whatevergreen/releases))

### ACPI

- SSDT-AWAC.aml [SSDT-PNLF-CFL.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-AWAC.dsl)
- SSDT-EC-USBX.aml [SSDT-EC-USBX.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-EC-USBX.dsl)
- SSDT-GPI0.aml [SSDT-GPI0.dsl](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/decompiled/SSDT-GPI0.dsl)
- SSDT-PLUG.aml [SSDT-PLUG.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-PLUG.dsl)
- SSDT-PNLF-CFL.aml [SSDT-PNLF-CFL.dsl](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/decompiled/SSDT-PNLF-CFL.dsl)

All dsl files downloaded and compiled 07 07 2020. 

