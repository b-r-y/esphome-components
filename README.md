# ESPHome components

This repository contains custom ESPHome components.
Currently supported are:

* Wavin AHC9000

    All credit goes to:

    * https://github.com/heinekmadsen

    and

    * https://github.com/nic6911

    Check out their work and you will find a lot more than what is here.

# Notes on Hardware

To make your life easy use the HW described and provided by https://github.com/nic6911.

Alternatively, I used the following:

* ESP32-WROOM - development board like this one: [ESP32-WROOM](https://www.amazon.de/-/en/dp/B0D4QZ9CKD?ref=ppx_yo2ov_dt_b_fed_asin_title)
* 3.3V TTL to RS485 like this one: [TTL to RS485](https://www.amazon.de/-/en/dp/B09VGJCJKQ?ref=ppx_yo2ov_dt_b_fed_asin_title)
* DC-DC buck ~4-30V down to 3.3V like this one: [DC-DC 5-30V in 3.3V out](https://www.aliexpress.com/item/1005006486270630.html?spm=a2g0o.productlist.main.3.2f123ab55c8Ymr&algo_pvid=5e64a96c-db1d-4b61-8346-436233c32f2c&algo_exp_id=5e64a96c-db1d-4b61-8346-436233c32f2c-1&pdp_ext_f=%7B%22order%22%3A%223061%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21DKK%2132.19%217.25%21%21%2131.91%217.18%21%402141001d17402102246237872e307a%2112000037383092779%21sea%21DK%210%21ABX&curPageLogUid=sJNy2Mu2Vkfk&utparam-url=scene%3Asearch%7Cquery_from%3A)


# Example ESPHome yaml config

```yaml
esphome:
  name: wavin
  friendly_name: "Wavin"

esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable logging
logger:

# web_server:  # Uncomment this to publish on LAN
#   port: 80

# Enable Home Assistant API
api:
  encryption:
    key: !secret esphome_api_key

ota:
  - platform: esphome

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Wavin Fallback Hotspot"
    password: "some fallback password"

captive_portal:

substitutions:
  # UNIQUE NAME FOR THE DEVICE
  device: wavin # Case sensitive!!!
  name: Wavin   # "Friendly name" - not case sensitive!!!

  # CHANNEL friendly names (If using spaces remember to add ")
  channel_01_friendly_name: "Channel 01"
  channel_02_friendly_name: "Channel 02"
  channel_03_friendly_name: "Channel 03"
  channel_04_friendly_name: "Channel 04"
  channel_05_friendly_name: "Channel 05"
  channel_06_friendly_name: "Channel 06"
  channel_07_friendly_name: "Channel 07"
  channel_08_friendly_name: "Channel 08"
  channel_09_friendly_name: "Channel 09"
  channel_10_friendly_name: "Channel 10"
  channel_11_friendly_name: "Channel 11"
  channel_12_friendly_name: "Channel 12"
  channel_13_friendly_name: "Channel 13"
  channel_14_friendly_name: "Channel 14"
  channel_15_friendly_name: "Channel 15"
  channel_16_friendly_name: "Channel 16"

  # CHANNEL ID´S (ONLY LOWER CASE LETTERS, NO SPACES) used for entity ids
  channel_01_id: channel_01
  channel_02_id: channel_02
  channel_03_id: channel_03
  channel_04_id: channel_04
  channel_05_id: channel_05
  channel_06_id: channel_06
  channel_07_id: channel_07
  channel_08_id: channel_08
  channel_09_id: channel_09
  channel_10_id: channel_10
  channel_11_id: channel_11
  channel_12_id: channel_12
  channel_13_id: channel_13
  channel_14_id: channel_14
  channel_15_id: channel_15
  channel_16_id: channel_16

  # CHANNEL Alignments (ONLY change if you have offsets in channel vs temperature. Some have reported this if using multiple strings pr. room thermostat)
  channel_01_sensor: "0x00"
  channel_02_sensor: "0x01"
  channel_03_sensor: "0x02"
  channel_04_sensor: "0x03"
  channel_05_sensor: "0x04"
  channel_06_sensor: "0x05"
  channel_07_sensor: "0x06"
  channel_08_sensor: "0x07"
  channel_09_sensor: "0x08"
  channel_10_sensor: "0x09"
  channel_11_sensor: "0x0A"
  channel_12_sensor: "0x0B"
  channel_13_sensor: "0x0C"
  channel_14_sensor: "0x0D"
  channel_15_sensor: "0x0E"
  channel_16_sensor: "0x0F"

  channel_01: "0x00"
  channel_02: "0x01"
  channel_03: "0x02"
  channel_04: "0x03"
  channel_05: "0x04"
  channel_06: "0x05"
  channel_07: "0x06"
  channel_08: "0x07"
  channel_09: "0x08"
  channel_10: "0x09"
  channel_11: "0x0A"
  channel_12: "0x0B"
  channel_13: "0x0C"
  channel_14: "0x0D"
  channel_15: "0x0E"
  channel_16: "0x0F"

# Uncomment the active channels on your Wavin Ahc 9000
packages:
  # _base_: !include common/__base__.yaml
  remote_package:
    url: https://github.com/b-r-y/esphome-components
    ref: main
    files:
      - components/wavinahc9000/configs/main.yaml
      - components/wavinahc9000/configs/channel_01.yaml
      - components/wavinahc9000/configs/channel_01_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_02.yaml
      - components/wavinahc9000/configs/channel_02_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_03.yaml
      - components/wavinahc9000/configs/channel_03_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_04.yaml
      - components/wavinahc9000/configs/channel_04_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_05.yaml
      - components/wavinahc9000/configs/channel_05_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_06.yaml
      - components/wavinahc9000/configs/channel_06_comfort.yaml # Only for channels with thermostat with IR sensor
      - components/wavinahc9000/configs/channel_07.yaml
      - components/wavinahc9000/configs/channel_07_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_08.yaml
      #- components/wavinahc9000/configs/channel_08_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_09.yaml
      #- components/wavinahc9000/configs/channel_09_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_10.yaml
      #- components/wavinahc9000/configs/channel_10_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_11.yaml
      #- components/wavinahc9000/configs/channel_11_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_12.yaml
      #- components/wavinahc9000/configs/channel_12_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_13.yaml
      #- components/wavinahc9000/configs/channel_13_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_14.yaml
      #- components/wavinahc9000/configs/channel_14_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_15.yaml
      #- components/wavinahc9000/configs/channel_15_comfort.yaml # Only for channels with thermostat with IR sensor
      #- components/wavinahc9000/configs/channel_16.yaml
      #- components/wavinahc9000/configs/channel_16_comfort.yaml # Only for channels with thermostat with IR sensor
    refresh: 0s

uart:
  - id: uart_${device}
    rx_pin: GPIO16
    tx_pin: GPIO17
    baud_rate: 38400
    stop_bits: 1
    parity: NONE
```

