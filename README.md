super-pom
=========

The shared master pom for all DBC Java projects.

The purpose of this pom is to:

* setup repositories for dependency resolution and artifact distribution
* control the JDK version used across all DBC projects
* ensure Git branch and commit information is available in artifact MANIFEST.MF file

**Remember** to update the CHANGELOG.md file on **every pull request**

version-validation
------------------

`version-check.py` is used with an effective pom, (`mvn -Doutput=effective-pom.xml help:effective-pom`), to check against newest known versions of the user plugins/dependencies.

When you need to lock a dependency, you can use `ignore-versions.csv`.
The first two columns are:

 * `groupId` or `groupId.*`, for each dependency/plugin groupId is used, end then parent groupIds with `.*` to locate an ignore list
 * `artifactId` or `*` , try first exact then wildcard, when looking for an ignore list

The rest of the columns are release/snapshot versions to ignore **OR** one `*`, which says no version checking. This is used when versions are defined by by 3rd party. i.e.

Eclipselink version is taken from payara and so is all of jackson:
```
org.eclipse.persistence, eclipselink, *
com.fasterxml.jackson.*, *, *
```

We want to ignore release a candidate and a milestone release for jupiter, but be informed when a new version is available:
```
org.junit.jupiter, *, 5.9.0-RC1, 5.9.0-M1
```
