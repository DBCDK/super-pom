super-pom
=========

The shared master pom for all DBC Java projects.

The purpose of this pom is to:

* setup repositories for dependency resolution and artifact distribution
* control the JDK version used across all DBC projects
* ensure Git branch and commit information is available in artifact MANIFEST.MF file

**Remember** to update the CHANGELOG.md file on **every pull request** 

### How to Do a new version

In a fresh master just run `./do-release.sh`. 

If a specific old name is wanted specify it as the first argument to 
the script, or else it defaults to current week.

```bash
./do-release.sh
```                       
                                                               
