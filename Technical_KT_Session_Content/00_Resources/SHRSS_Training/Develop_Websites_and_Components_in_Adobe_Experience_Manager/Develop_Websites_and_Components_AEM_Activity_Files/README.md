# We.Train site
**ADLS Course:** Develop Websites and Components

## Version Compatibility
The maven generate scripts for this project are located in the [training-files/archetype-scripts](training-files/archetype-scripts) folder. This project is compatible with:
 * Azul Zulu JDK 11 or Oracle JDK 11
 * Archetype 39
 * Core Components 2.19.2
 * WKND 1.0.0, 2.1.0+
 * AEM 6.5 with Service Pack 13+
 * AEM Cloud Service 2022.10.9398.20221020T071514Z-220800
 * Visual Studio Code or Eclipse
 * Maven: 3.3.9+
 * Node: 13.7.0+
 * NPM: 6.13.6+

## Run this code locally
> Note: this code depends on the [WKND site](https://github.com/adobe/aem-guides-wknd/releases/latest) being installed. Make sure WKND is installed prior to installing this code

### AEM as a Cloud Service
 1. Download the latest quickstart jar
 1. Open a terminal to the unzipped SDK
 2. Run 
    ```
    java -jar aem-sdk-quickstart-< BUILD >.jar -r author,dev,dynamicmedia_scene7 -p 4502 -gui
    ```
 3. Once installed, open a terminal to the root directory of this project
 4. Run 
    ```
    mvn clean install -Padobe-public,autoInstallSinglePackage
    ```
### AEM 6.5.x
 1. Download AEM 6.5 and SP (see above)
 2. Creat a folder and add the 6.5 jar and license.properties file
    1. Create a subfolder called **crx-quickstart/install**
    2. Add the service pack zip to th install folder
 3. Open a terminal to the folder containing the 6.5 jar
 4. Run 
    ```
    java -jar aem-quickstart.jar -r author,dev,dynamicmedia_scene7 -p 4502 -gui
    ```
 3. Once installed, open a terminal to the root directory of this project
 6. Run 
    ```
    mvn clean install -Padobe-public,autoInstallSinglePackage,classic
    ```

## Maven Modules

The main parts of the template are:

* core: Java bundle containing all core functionality like OSGi services, listeners or schedulers, as well as component-related Java code such as servlets or request filters.
* it.tests: Java based integration tests
* ui.apps: contains the /apps (and /etc) parts of the project, ie JS&CSS clientlibs, components, and templates
* ui.content: contains sample content using the components from the ui.apps
* ui.config: contains runmode specific OSGi configs for the project
* ui.frontend: contains custom Style Code (SCSS, LESS, or CSS) and clientside JS code. Compiled via Webpack into an AEM clientlibrary under ui.apps
* ui.tests: Selenium based UI tests
* all: a single content package that embeds all of the compiled modules (bundles and content packages) including any vendor dependencies

## Maven Profiles
* `autoInstallSinglePackage` - Installs the all container package on author that includes
  * All maven modules in this project
  * All 3rd party packages such as core components and WKND

* `autoInstallSinglePackagePublish` - Installs the all container package on publish

* `classic` - a non archetype standard profile that allows certain dependencies to be installed for AEM 6.5 rather than Cloud Service.

Compile ui.frontend to an AEM clientlibrary under ui.apps. This must be run against ui.frontend directory.
    
    npm run dev or npm run prod

To build all the modules and deploy the `all` package to a local instance of AEM, run in the project root directory the following command:

    mvn clean install -PautoInstallSinglePackage

Or to deploy it to a publish instance, run

    mvn clean install -PautoInstallSinglePackagePublish

Or alternatively

    mvn clean install -PautoInstallSinglePackage -Daem.port=4503

Or to deploy only the bundle to the author, run

    mvn clean install -PautoInstallBundle

Or to deploy only a single content package, run in the sub-module directory (i.e `ui.apps`)

    mvn clean install -PautoInstallPackage

## Testing

There are three levels of testing contained in the project:

### Unit tests

This show-cases classic unit testing of the code contained in the bundle. To
test, execute:

    mvn clean test

### Integration tests

This allows running integration tests that exercise the capabilities of AEM via
HTTP calls to its API. To run the integration tests, run:

    mvn clean verify -Plocal

Test classes must be saved in the `src/main/java` directory (or any of its
subdirectories), and must be contained in files matching the pattern `*IT.java`.

The configuration provides sensible defaults for a typical local installation of
AEM. If you want to point the integration tests to different AEM author and
publish instances, you can use the following system properties via Maven's `-D`
flag.

| Property | Description | Default value |
| --- | --- | --- |
| `it.author.url` | URL of the author instance | `http://localhost:4502` |
| `it.author.user` | Admin user for the author instance | `admin` |
| `it.author.password` | Password of the admin user for the author instance | `admin` |
| `it.publish.url` | URL of the publish instance | `http://localhost:4503` |
| `it.publish.user` | Admin user for the publish instance | `admin` |
| `it.publish.password` | Password of the admin user for the publish instance | `admin` |

The integration tests in this archetype use the [AEM Testing
Clients](https://github.com/adobe/aem-testing-clients) and showcase some
recommended [best
practices](https://github.com/adobe/aem-testing-clients/wiki/Best-practices) to
be put in use when writing integration tests for AEM.

## Static Analysis

The `analyse` module performs static analysis on the project for deploying into AEMaaCS. It is automatically
run when executing

    mvn clean install

from the project root directory. Additional information about this analysis and how to further configure it
can be found here https://github.com/adobe/aemanalyser-maven-plugin

### UI tests

They will test the UI layer of your AEM application using Selenium technology. 

To run them locally:

    mvn clean verify -Pui-tests-local-execution

This default command requires:
* an AEM author instance available at http://localhost:4502 (with the whole project built and deployed on it, see `How to build` section above)
* Chrome browser installed at default location

Check README file in `ui.tests` module for more details.

## ClientLibs

The frontend module is made available using an [AEM ClientLib](https://helpx.adobe.com/experience-manager/6-5/sites/developing/using/clientlibs.html). When executing the NPM build script, the app is built and the [`aem-clientlib-generator`](https://github.com/wcm-io-frontend/aem-clientlib-generator) package takes the resulting build output and transforms it into such a ClientLib.

A ClientLib will consist of the following files and directories:

- `css/`: CSS files which can be requested in the HTML
- `css.txt` (tells AEM the order and names of files in `css/` so they can be merged)
- `js/`: JavaScript files which can be requested in the HTML
- `js.txt` (tells AEM the order and names of files in `js/` so they can be merged
- `resources/`: Source maps, non-entrypoint code chunks (resulting from code splitting), static assets (e.g. icons), etc.