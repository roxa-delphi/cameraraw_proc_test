Name
  cameraraw_proc_test

Overview
  CAMERA RAW file processing test used rawpy and numpy

Description
  RAW file process is composed by following process.
    1. Black level correction
    2. Demosaic
    3. Whilte balance correction
    4. Color matrix correction
    5. Gamma correction

  This test used PENTAX raw file (*.PEF).

  raw_info.py
    Print RAW file informations.

  try1.py
    Read RAW file and output PNG file without any corrections.
    Output file is try1.png.

  try2.py
    Add black level corection.
    Output file is try2.png.

  try3.py
    Add easy demosaic.
    Output file is try3.png.

  try4.py
    Add white balance correction.
    Output file is try4.png.

  try5.py
    Add gamma correction.
    Output file is try5.png.

Requirement
  Python3
  rawpy module
  numpy module
  imageio module

License

Author
  https://github.com/roxa-delphi

