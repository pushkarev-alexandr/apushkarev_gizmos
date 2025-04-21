# Nuke apushkarev_gizmos
## Установка:
1. **Найдите папку `.nuke`:**
   
   Она находится в домашней директории пользователя:
   - **Windows:** `C:\Users\<ваше_имя>\.nuke`
   - **macOS/Linux:** `/home/<ваше_имя>/.nuke` или `~/.nuke`
2. **Склонируйте репозиторий в `.nuke`:**
   ```sh
   git clone https://github.com/pushkarev-alexandr/apushkarev_gizmos.git
   ```
   Или скачайте архив с GitHub и распакуйте его в папку `.nuke`.
3. Добавьте путь к гизмам в `menu.py`:
   
   В файле `.nuke/menu.py` добавьте строку:
   ```python
   nuke.pluginAddPath('./apushkarev_gizmos')
   ```
   Если файл menu.py отсутствует, просто создайте его и добавьте туда эту строку.
## Содержимое:
### 3D
- AOV_Sampler.gizmo
- CameraRelocator.gizmo
- CopyToPosition.gizmo
- PositionSampler.gizmo
### CG
- Normalize.gizmo
- SeamlessTexture.gizmo
- TangentWorldNormalConvert.gizmo
- TextureUnwraper.gizmo
- UnwrapTexture.gizmo
### Channel
- Set Alpha.nk
### Check
- CheckNegative.gizmo
- ExamineShot.gizmo
- TrackCheck.gizmo
### Color
- ChannelToRGB.gizmo
- HueSaturationTransfer.gizmo
- matchBlackWhitePoint.gizmo
### Draw
- AddGrain.gizmo
- RandomWindows.gizmo
- ScatterImg.gizmo
- StrokeAnimation.nk
- TexturePainter.gizmo
### Filter
- ExponentialBlur.gizmo
- GodRaysSmoothed.gizmo
- TinyHolesRemove.gizmo
### Keying
- ChromakeyTimeEcho.gizmo
- DifferenceKeyer.gizmo
- DifferenceThreshold.gizmo
- SampleRamp.gizmo
- ScreenSaturation.gizmo
- ScreenSaturationBoost.gizmo
- SmartIBK.gizmo
### Merge
- ContactSheetToSequence.gizmo
- SequenceToContactSheet.gizmo
### ProPainter
- ProPainterComfyUI.gizmo
### ReadWrite
- ReadFolder.nk
- WriteFolder.nk
### Time
- SimpleLoopDissolve.gizmo
- TimeEchoBidirectional.gizmo
### Transform
- CardPlacer.gizmo
- CornerPin_from_Position_pass.gizmo
- CornerPin_from_UV.gizmo
- Mirror_AE.gizmo
- ReformatUniscale.nk
- RotateImage.gizmo
- Tracker_from_Position_pass.gizmo
- Tracker_from_UV.gizmo
- TransformMaskedSmooth.gizmo
- UnfoldEdges.gizmo
### Utilities
- ConformRetime.gizmo
- FineTune.gizmo
- KeepBBox.nk
- RandomFrame.nk
- Store Selection.nk
- TechCheck.gizmo
- ToDoList.nk
- ValuesRandomizer.nk
