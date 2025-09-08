# Mystery Trackers Save Game Patcher

This patcher will enable edited save game files to work.
The current issue is that all game save files have a checksum at the begining of each file. This calculation is verified when the game launches and if the number does not calculate the game save will not work.

This patch when run will calculate the file checksum and patch the savegame file, you can then use that patched save game file to continue your journey through the **Mystery Trackers**  find object game.

These games store a checksum inside an XML comment like:

```xml
<!--7070940-->

This tool fixes the checksum in **Mystery Trackers** save game files so you can safely edit them.

---

## 🚀 Usage

1. Copy your save file (e.g., `myeditedsavefile.xml`) into the same folder as this python script folder.  
2. Run the patcher:

```bash
python hex.py myeditedsavegame.xml

3. you can then put the patched save game file in with the other save game files.
