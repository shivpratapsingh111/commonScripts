### Exclude Nuclei Templates based on IDs
 
- organiseNuclei.py - Excludes unwanted nuclei templates (Moves them into **.excludedNucleiTemplates/**, hidden in linux)

- id.txt - contains IDs to exclude (You can add more IDs to exclude)

### Usage:

- If your provide id.txt, then it will exclude all Nuclei Templates with id that matches in id.txt

    ```
    python3 organiseTemplates.py -dir /home/nuclei-templates -i id.txt
    ```
- If you don't provide id.txt then it will remove templates with IDs set by default in the script

    ```
    python3 organiseTemplates.py -dir /home/nuclei-templates
    ```

**Currently it only supports exclusion through IDs**

### Workflow:

- Retrives ID from file and if **-f** flag provided, else uses predefined array with IDs
- Makes **.excludedNucleiTemplates/** directory (hidden in linux)
- It matches id (string) with `id:` scalar in each and every template in provided directory and it's sub directory.
- Moves templates with matched id to **.excludedNucleiTemplates/** directory

### TODO

- [ ] Add support to exclusion through tags
- [ ] Implement multithreading
- [ ] Add flag to get back removed templates

---

## Open for contributions