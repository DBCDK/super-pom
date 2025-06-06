# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## latest
### Added
- flyway-database-postgresql for postgres specific classes
### Changed 
- JDK target set to 17
- Update flyway from 9.22.3 to 11.4.1
- Update jackson from 2.17.1 to 2.18.2
- Update jersey from 3.1.5 to 3.1.7
- Update postgresql-driver from 42.7.3 to 42.7.5
- Update smallrye-graphql from 2.8.6 to 2.12.2
- Update snakeyaml from 2.2 to 2.3
- Update junit5 from 5.10.3 to 5.11.4
- Update mockito from 5.12.0 to 5.16.1
- Update testcontainers from 1.19.8 to 1.20.6
- Update wiremock from 3.8.0 to 3.12.1
- Update maven-compiler-plugin from 3.13.0 to 3.14.0
- Update maven-deploy-plugin from 3.1.2 to 3.1.4
- Update maven-dependency-plugin from 3.7.1 to 3.8.1
- Update exec-maven-plugin from 3.3.0 to 3.5.0
- Update maven-surefire-plugin from 3.3.0 to 3.5.2
- Update maven-failsafe-plugin from 3.3.0 to 3.5.2
- Update maven-pmd-plugin from 3.21.0 to 3.26.0
- Update sonar-maven-plugin from 3.9.1.2184 to 5.0.0.4389

## old-202517
- No Changes

## old-202447
### Added
- Add git-commit-id-maven-plugin (replaces git-commit-id-plugin)
- Add maven-deploy-plugin
- Add maven-dependency-plugin
- Add exec-maven-plugin
- Add maven-resources-plugin
- Add org.wiremock:wiremock dependency
### Changed
- Update hazelcast version from 5.3.1 to 5.3.6 [hazelcast release notes](https://docs.hazelcast.com/hazelcast/5.3/release-notes/5-3-6)
- Update jackson version from 2.15.0 to 2.17.1 [jackson release notes](https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.17)
- Update jakarta.xml.bind-api and jaxb-impl version from 4.0.0 to 4.0.1
- Update jersey version from 3.1.0 to 3.1.5 [jersey release notes](https://github.com/eclipse-ee4j/jersey/releases/tag/3.1.5)
- Update junit5 version from 5.10.0 to 5.10.3 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.10.3)
- Update kafka-clients version from 3.6.0 to 3.7.1 [kafka release notes](https://archive.apache.org/dist/kafka/3.7.1/RELEASE_NOTES.html)
- Update maven-compiler-plugin version from 3.11.0 to 3.13.0 [release notes](https://github.com/apache/maven-compiler-plugin/releases/tag/maven-compiler-plugin-3.13.0)
- Update maven-enforcer-plugin version from 3.4.1 to 3.5.0
- Update maven-failsafe-plugin version from 3.2.1 to 3.3.0
- Update maven-jar-plugin from 3.3.0 to 3.4.2 [maven-jar-plugin release notes](https://github.com/apache/maven-jar-plugin/releases/tag/maven-jar-plugin-3.4.2)
- Update maven-surefire-plugin version from 3.2.1 to 3.3.0 [release notes](https://github.com/apache/maven-surefire/releases/tag/surefire-3.3.0)
- Update mockito version from 5.6.0 to 5.12.0 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v5.12.0)
- Update postgresql driver version from 42.6.0 to 42.7.3 [postgresql release notes](https://jdbc.postgresql.org/changelogs/)
- Update smallrye-graphql-servlet and smallrye-graphql-ui-graphiql version from 2.2.3 to 2.8.6 [smallrye-graphql](https://smallrye.io/smallrye-graphql)
- Update snakeyaml version from 2.0 to 2.2 [snakeyaml release notes](https://bitbucket.org/snakeyaml/snakeyaml/wiki/Changes)
- Update testcontainers version from 1.19.1 to 1.19.8 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.19.8)

## old-202437
- No changes
 
## old-202420
### Added
- Add javax.cache.cache-api dependency
- Add polyglot and js-community dependencies for GraalVM JavaScript embedding
- Add standalone nashorn-core dependency
### Changed
- Update eclipselink version from 4.0.0 to 4.0.1 [eclipselink release notes](https://www.eclipse.org/eclipselink/releases/4.0.php)
- Update flyway version from 9.11.0 9.22.3 [flyway release notes](https://documentation.red-gate.com/fd/release-notes-for-flyway-engine-179732572.html)
- Update hazelcast version from 5.1.1 to 5.3.1 [hazelcast release notes](https://docs.hazelcast.com/hazelcast/5.3/release-notes/5-3-1)
- Update jackson version from 2.13.4 to 2.15.0 [jackson release notes](https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.15)
- Update junit5 version from 5.9.1 to 5.10.0 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.10.0)
- Update kafka-clients version from 3.3.0 to 3.6.0 [kafka release notes](https://archive.apache.org/dist/kafka/3.6.0/RELEASE_NOTES.html)
- Update maven-failsafe-plugin version from 3.0.0 to 3.2.1 [release notes](https://github.com/apache/maven-surefire/releases/tag/surefire-3.2.1)
- Update maven-pmd-plugin version from 3.20.0 to 3.21.0 [release notes](https://maven.apache.org/plugins/maven-pmd-plugin/releasenotes.html#version-3-21-0)
- Update maven-surefire-plugin version from 3.0.0 to 3.2.1 [release notes](https://github.com/apache/maven-surefire/releases/tag/surefire-3.2.1)
- Update microprofile version from 5.0 to 6.1 [microprofile release notes](https://github.com/eclipse/microprofile/releases/tag/6.1)
- Update mockito version from 4.11.0 to 5.6.0 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v5.6.0)
- Update postgresql driver version from 42.5.1 to 42.6.0 [postgresql release notes](https://jdbc.postgresql.org/changelogs/)
- Update smallrye-graphql-servlet and smallrye-graphql-ui-graphiql version from 2.0.1 to 2.2.3 [smallrye-graphql](https://smallrye.io/smallrye-graphql)
- Update snakeyaml version from 1.33 to 2.0 [snakeyaml release notes](https://bitbucket.org/snakeyaml/snakeyaml/wiki/Changes)
- Update spotbugs-annotations from 4.7.3 to 4.8.0 [spotbugs release notes](https://github.com/spotbugs/spotbugs/releases/tag/4.8.0)
- Update spotbugs-maven-plugin version 4.7.3.0 to 4.7.3.6 [spotbugs maven plugin release notes](https://github.com/spotbugs/spotbugs-maven-plugin/releases/tag/spotbugs-maven-plugin-4.7.3.6)
- Update testcontainers version from 1.17.6 to 1.19.1 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.19.1)

## old-202409
### Added
- sonarcube sonar.host.url, sonar.java.binaries, and sonar.source default properties
- sonar-maven-plugin

## old-202338
### Added
- Add maven-failsafe-plugin dependency
### Changed
- Update maven-compiler-plugin version from 3.8.1 to 3.11.0 [release notes](https://github.com/apache/maven-compiler-plugin/releases/tag/maven-compiler-plugin-3.11.0)
- Update maven-pmd-plugin version from 3.17.0 to 3.20.0 [release notes](https://maven.apache.org/plugins/maven-pmd-plugin/releasenotes.html#version-3-20-0)
- Update maven-surefire-plugin version from 2.22.2 to 3.0.0 [release notes](https://github.com/apache/maven-surefire/releases/tag/surefire-3.0.0)

## old-202332
### Added
- Add jakarta.jakartaee-core-api dependency
- Add jakarta.xml.bind-api and jaxb-impl dependencies
### Changed
- Update eclipselink version from 2.7.9 to 4.0.0 [eclipselink release notes](https://www.eclipse.org/eclipselink/releases/4.0.php)
- Update flyway version from 9.0.4 to 9.11.0 [flyway release notes](https://documentation.red-gate.com/fd/release-notes-for-flyway-engine-179732572.html)
- Update hazelcast version from 4.2 to 5.1.1 [hazelcast release notes](https://docs.hazelcast.com/hazelcast/5.1/release-notes/5-1-1)
- Update jackson version from 2.12.7 to 2.13.4 [jackson release notes](https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.13.4)
- Update jakartaee version from 8.0.0 to 10.0.0
- Update jersey version from 2.36 to 3.1.0 [jersey release notes](https://github.com/eclipse-ee4j/jersey/releases/tag/3.1.0)
- Update junit5 version from 5.9.0 to 5.9.1 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.9.1)
- Update logback version from 1.2.3 to 1.2.11 [logback release notes](https://logback.qos.ch/news.html#1.2.11)
- Update maven-enforcer-plugin version from 3.0.0 to 3.2.1
- Update microprofile version from 4.1 to 5.0 [microprofile release notes](https://github.com/eclipse/microprofile/releases/tag/5.0)
- Update mockito version from 4.6.1 to 4.11.0 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v4.11.0)
- Update postgresql driver version from 42.5.0 to 42.5.1 [postgresql release notes](https://jdbc.postgresql.org/changelogs/)
- Update slf4j version from 1.7.32 to 1.7.36 [slf4j release notes](https://www.slf4j.org/news.html#1.7.36)
- Update smallrye-graphql-servlet and smallrye-graphql-ui-graphiql version from 1.6.0 to 2.0.1 [smallrye-graphql](https://smallrye.io/smallrye-graphql/2.0.1/)
- Update snakeyaml version from 1.28 to 1.33 [snakeyaml release notes](https://bitbucket.org/snakeyaml/snakeyaml/wiki/Changes)
- Update spotbugs-maven-plugin version from 4.7.2.2 to 4.7.3.0 [spotbugs maven plugin release notes](https://github.com/spotbugs/spotbugs-maven-plugin/releases/tag/spotbugs-maven-plugin-4.7.3.0)
- Update testcontainers version from 1.17.3 to 1.17.6 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.17.6)
### Removed
- Remove otj-pg-embedded dependency, use [dbc-commons-testcontainers-postgres](https://gitlab.dbc.dk/pu/test/dbc-commons-testcontainers-postgres) instead

## old-payara5
### Changed
- jersey version updated from 2.34 to 2.36
- spotbugs-annotations updated from 4.5.3 to 4.7.3 [spotbugs release notes](https://github.com/spotbugs/spotbugs/releases/tag/4.7.3)
- spotbugs-maven-plugin updated from 4.5.3.0 to 4.7.2.2 [spotbugs maven plugin release notes](https://github.com/spotbugs/spotbugs-maven-plugin/releases/tag/spotbugs-maven-plugin-4.7.2.2)

## old-202246
### Added
- kafka-clients 3.3.0 [kafka release notes](https://archive.apache.org/dist/kafka/3.3.0/RELEASE_NOTES.html)
### Changed
- Update postgresql driver version from 42.3.2 to 42.5.0 [postgresql release notes](https://jdbc.postgresql.org/changelogs/)

## old-202241
- No changes

## old-202239
- No changes

## old-202236
### Added
- maven-pmd-plugin 3.17.0
- smallrye-graphql-servlet and smallrye-graphql-ui-graphiql dependencies [smallrye-graphql](https://smallrye.io/smallrye-graphql/1.6.0/)
### Changed
- Update flyway version from 8.5.0 to 9.0.4 [flyway release notes](https://flywaydb.org/documentation/learnmore/releaseNotes.html#9.0.4)
- Update jackson version from 2.12.4 to 2.12.7 [jackson release notes](https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.12.4)
- Update junit5 version from 5.8.2 to 5.9.0 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.9.0)
- Update mockito version from 4.3.1 to 4.6.1 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v4.6.1)
- Update testcontainers version from 1.16.3 to 1.17.3 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.17.3)

## old-202232
- No changes

## old-202213
### Changed
- Update eclipselink version from 2.7.7 to 2.7.9
- Update flyway version from 8.0.2 to 8.5.0 [flyway release notes](https://flywaydb.org/documentation/learnmore/releaseNotes.html#8.5.0)
- Update junit5 version from 5.8.1 to 5.8.2 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.8.2)
- Update mockito version from 3.12.4 to 4.3.1 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v4.3.1)
- Update postgresql driver version from 42.3.1 to 42.3.2 [postrgesql release notes](https://jdbc.postgresql.org/documentation/changelog.html#version_42.3.2)
- Update spotbugs.plugin.version from 4.4.2.2 to 4.5.3.0
- Update spotbugs.annotations.version from 4.4.2 to 4.5.3
- Update testcontainers version from 1.16.2 to 1.16.3 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.16.3)

## old-202210
### Changed
- Update flyway version from 7.5.3 to 8.0.2 [flyway release notes](https://flywaydb.org/documentation/learnmore/releaseNotes.html#8.0.2)
- Update hazelcast version from 3.12.6 to 4.2 [hazelcast release notes](https://docs.hazelcast.org/docs/rn/#4-2)
- Update jackson version from 2.10.2 to 2.12.4 [jackson release notes](https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.12.4)
- Update jersey version from 2.30 to 2.34 [jersey release notes](https://eclipse-ee4j.github.io/jersey.github.io/release-notes/2.34.html)
- Update junit4 version from 4.13.1 to 4.13.2 [junit4 release notes](https://github.com/junit-team/junit4/blob/HEAD/doc/ReleaseNotes4.13.2.md)
- Update junit5 version from 5.7.1 to 5.8.1 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.8.1)
- Update microprofile version from 3.3 to 4.1 [microprofile release notes](https://github.com/eclipse/microprofile/releases/tag/4.1)
- Update mockito version from 3.7.7 to 3.12.4 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v3.12.4)
- Update postgresql driver version from 42.2.18 to 42.3.1 [postrgesql release notes](https://jdbc.postgresql.org/documentation/changelog.html#version_42.3.1)
- Update slf4j version from 1.7.30 to 1.7.32 [slf4j release notes](http://www.slf4j.org/news.html)
- Update snakeyaml version from 1.25 to 1.28 [snakeyaml release notes](https://bitbucket.org/asomov/snakeyaml/wiki/Changes)
- Update spotbugs.annotations.version from 4.2.1 to 4.4.2
- Update spotbugs.plugin.version from 4.2.0 to 4.4.2.2
- Update testcontainers version from 1.15.1 to 1.16.2 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.16.2)

## old-202149
### Added
- junit-jupiter-params dependency

## old-202116
### Changed
- Update flyway version from 7.2.0 to 7.5.3 [flyway release notes](https://flywaydb.org/documentation/learnmore/releaseNotes.html#7.5.3)
- Update junit5 version from 5.7.0 to 5.7.1 [junit5 release notes](https://junit.org/junit5/docs/current/release-notes/index.html#release-notes-5.7.1).
- Update mockito version from 3.6.0 to 3.7.7 [mockito release notes](https://github.com/mockito/mockito/releases/tag/v3.7.7)
- Update spotbugs.annotations.version from 4.1.4 to 4.2.1
- Update spotbugs.plugin.version from 4.1.4 to 4.2.0
- Update testcontainers version from 1.15.0 to 1.15.1 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.15.1)
- Update maven git-commit-id-plugin from 3.0.1 to 4.0.3 [git-commit-id-plugin release notes](https://github.com/git-commit-id/git-commit-id-maven-plugin/releases/tag/v4.0.3)
- Update maven-compiler-plugin from 3.8.0 to 3.8.1 [maven-compiler-plugin release notes](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12317225&version=12343484)
- Update maven-jar-plugin from 3.1.2 to 3.2.0 [maven-jar-plugin release notes](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12317526&version=12345503)

## old-202107
### Added
- Dependencies from microservice-pom
- surefire and spotbugs plugins from microservice-pom
### Changed
- Update flyway version from 7.0.4 to 7.2.0 [flyway release notes](https://flywaydb.org/documentation/learnmore/releaseNotes.html#7.2.0)
- Update mockito version from 3.5.15 to 3.6.0 [mockito release notes](https://github.com/mockito/mockito/blob/release/3.x/doc/release-notes/official.md#360)
- Update spotbugs.annotations.version from 4.1.2 to 4.1.4
- Update spotbugs.plugin.version from 4.0.4 to 4.1.4
- Update testcontainers version from 1.14.3 to 1.15.0 [testcontainers release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/1.15.0)

## master
### Added
- Initial version.
