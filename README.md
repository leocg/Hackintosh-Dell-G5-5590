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

**WIP**

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

