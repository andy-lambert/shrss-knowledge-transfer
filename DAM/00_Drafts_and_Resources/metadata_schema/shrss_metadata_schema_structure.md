# SHRSS metadata schema structure

Configuration details at each level. Source: consolidated `.content.xml` in this directory.

JCR path: `/conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`

---

## Root (jcr:root)

**primaryType:** `sling:OrderedFolder` · **title:** `shrssmetadataschema`

## image

### items

#### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

##### items

**primaryType:** `nt:unstructured`

###### tab1

**resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

- **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **items** — **primaryType:** `nt:unstructured`

      - **width** — **fieldLabel:** `Width` · **max:** `{Double}10000.0` · **min:** `{Double}0.0` · **name:** `./jcr:content/metadata/tiff:ImageWidth` · **readOnly:** `{Boolean}true` · **typeHint:** `Long` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **id:** `Key-1380290948315` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `number` · **primaryType:** `nt:unstructured`

      - **height** — **fieldLabel:** `Height` · **max:** `{Double}10000.0` · **min:** `{Double}0.0` · **name:** `./jcr:content/metadata/tiff:ImageLength` · **readOnly:** `{Boolean}true` · **typeHint:** `Long` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **id:** `Key-1380291070446` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `number` · **primaryType:** `nt:unstructured`

  - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

###### tab2

**resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

- **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

### jpeg

#### items

##### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **tab1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

  - **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **location** — **fieldLabel:** `Location` · **name:** `./jcr:content/metadata/Iptc4xmpExt:LocationShown` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **id:** `Key-1380291374527` · **primaryType:** `nt:unstructured`

          *(1 child nodes)*

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

- **tab2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

  - **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

### tiff

#### items

##### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **tab1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

  - **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **location** — **fieldLabel:** `Location` · **name:** `./jcr:content/metadata/Iptc4xmpExt:LocationShown` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **id:** `Key-1380291374527` · **primaryType:** `nt:unstructured`

          *(1 child nodes)*

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

- **tab2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

  - **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

## application

### pdf

#### items

##### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **tab1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

  - **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **pdftitle** — **fieldLabel:** `Pdf Title` · **name:** `./jcr:content/metadata/pdf:Title` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **id:** `Key-1380292819020` · **primaryType:** `nt:unstructured`

          *(1 child nodes)*

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

- **tab2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

  - **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **col1** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col2** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **col3** — **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

## video

### items

#### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

##### items

**primaryType:** `nt:unstructured`

###### tab1

**listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

- **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **items** — **primaryType:** `nt:unstructured`

      - **size** — **fieldLabel:** `Size` · **name:** `./jcr:content/metadata/size` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoDuration** — **fieldLabel:** `Duration (seconds)` · **name:** `./jcr:content/metadata/videoDuration` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **bitrate** — **fieldLabel:** `Total Bit Rate (kbps)` · **name:** `./jcr:content/metadata/bitrate` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoCodec** — **fieldLabel:** `Video Codec` · **name:** `./jcr:content/metadata/videoCodec` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoBitrate** — **fieldLabel:** `Video Bit Rate (kbps)` · **name:** `./jcr:content/metadata/videoBitrate` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **frameRate** — **fieldLabel:** `Video Frame Rate (fps)` · **name:** `./jcr:content/metadata/frameRate` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioCodec** — **fieldLabel:** `Audio Codec` · **name:** `./jcr:content/metadata/audioCodec` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioBitrate** — **fieldLabel:** `Audio Bit Rate (kbps)` · **name:** `./jcr:content/metadata/audioBitrate` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioSampleRate** — **fieldLabel:** `Audio Sample Rate (hz)` · **name:** `./jcr:content/metadata/audioSampleRate` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioChannels** — **fieldLabel:** `Number Audio Channels` · **name:** `./jcr:content/metadata/audioChannels` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

  - **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

###### tab2

**listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

- **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **items** — **primaryType:** `nt:unstructured`

      - **header** — **fieldLabel:** `YouTube Publishing` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

      - **category** — **fieldLabel:** `YouTube Category` · **name:** `./jcr:content/metadata/dam:youtube_category` · **resourceType:** `granite/ui/components/coral/foundation/form/select` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/dam:youtube_category` · **metaType:** `dropdown` · **primaryType:** `nt:unstructured`

        - **items** — **primaryType:** `nt:unstructured`

          *(15 child nodes)*

      - **privacy** — **fieldLabel:** `YouTube Privacy` · **name:** `./jcr:content/metadata/dam:youtube_privacy` · **resourceType:** `granite/ui/components/coral/foundation/form/select` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/dam:youtube_privacy` · **metaType:** `dropdown` · **primaryType:** `nt:unstructured`

        - **items** — **primaryType:** `nt:unstructured`

          *(3 child nodes)*

      - **urls** — **fieldLabel:** `YouTube URL List` · **name:** `./jcr:content/metadata/dam:youtube_urls` · **resourceType:** `dam/gui/components/admin/youtubeurllist` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/dam:youtube_urls` · **metaType:** `youtubeurllist` · **primaryType:** `nt:unstructured`

## dm_video

### items

#### tabs

**resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

##### items

**primaryType:** `nt:unstructured`

###### tab1

**listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

- **data** — **tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **items** — **primaryType:** `nt:unstructured`

      - **size** — **fieldLabel:** `Size` · **name:** `./jcr:content/metadata/dam:size` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoDuration** — **fieldLabel:** `Duration (seconds)` · **name:** `./jcr:content/metadata/duration` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **bitrate** — **fieldLabel:** `Total Bit Rate (kbps)` · **name:** `Total Stream Bit Rate` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoCodec** — **fieldLabel:** `Video Codec` · **name:** `Video Codec` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **videoBitrate** — **fieldLabel:** `Video Bit Rate (kbps)` · **name:** `Video Bit Rate` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **frameRate** — **fieldLabel:** `Video Frame Rate (fps)` · **name:** `Video Frame Rate` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioCodec** — **fieldLabel:** `Audio Codec` · **name:** `Audio Codec` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioBitrate** — **fieldLabel:** `Audio Bit Rate (kbps)` · **name:** `Audio Bit Rate` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioSampleRate** — **fieldLabel:** `Audio Sample Rate (hz)` · **name:** `Audio Sample Rate` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

      - **audioChannels** — **fieldLabel:** `Number Audio Channels` · **name:** `Number Audio Channels` · **resourceType:** `dam/gui/components/s7dam/common/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `text` · **primaryType:** `nt:unstructured`

  - **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

###### tab2

**listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

- **data** — **tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

- **items** — **primaryType:** `nt:unstructured`

  - **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

    - **items** — **primaryType:** `nt:unstructured`

      - **header** — **fieldLabel:** `YouTube Publishing` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

      - **category** — **fieldLabel:** `YouTube Category` · **name:** `./jcr:content/metadata/dam:youtube_category` · **resourceType:** `granite/ui/components/coral/foundation/form/select` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `dropdown` · **primaryType:** `nt:unstructured`

        - **items** — **primaryType:** `nt:unstructured`

          *(15 child nodes)*

      - **privacy** — **fieldLabel:** `YouTube Privacy` · **name:** `./jcr:content/metadata/dam:youtube_privacy` · **resourceType:** `granite/ui/components/coral/foundation/form/select` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `dropdown` · **primaryType:** `nt:unstructured`

        - **items** — **primaryType:** `nt:unstructured`

          *(3 child nodes)*

      - **urls** — **fieldLabel:** `YouTube URL List` · **name:** `./jcr:content/metadata/dam:youtube_urls` · **resourceType:** `dam/gui/components/admin/youtubeurllist` · **primaryType:** `nt:unstructured`

        - **data** — **metaType:** `youtubeurllist` · **primaryType:** `nt:unstructured`

## content

**primaryType:** `nt:unstructured`

## items

**primaryType:** `nt:unstructured`

### tabs

**size:** `L` · **resourceType:** `granite/ui/components/coral/foundation/tabs` · **primaryType:** `nt:unstructured`

#### items

**primaryType:** `nt:unstructured`

##### tab1

**listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Basic`

###### data

**tabid:** `f84cc8d6-60ab-474e-bdf8-a0b7a434f289` · **primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **_x0031_770945616833** — **fieldLabel:** `Upload Details` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **_x0031_770945433163** — **fieldLabel:** `Uploaded By` · **name:** `./jcr:createdBy` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./jcr:createdBy` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Metadata` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **title** — **fieldLabel:** `Title` · **name:** `./jcr:content/metadata/dc:title` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:title` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **description** — **fieldLabel:** `Description` · **name:** `./jcr:content/metadata/dc:description` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:description` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **format** — **fieldLabel:** `Type` · **name:** `./jcr:content/metadata/dc:format` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:format` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **language** — **emptyText:** `Select Option` · **fieldLabel:** `Language` · **name:** `./jcr:content/metadata/dc:language` · **ordered:** `true` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/formfields/v2/metadataselect` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **choicesCascading:** `default` · **cq-msm-lockable:** `./metadata/dc:language` · **metaType:** `dropdown` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **ar_tn** — **text:** `Arabic (Tunisia)` · **value:** `ar_tn` · **primaryType:** `nt:unstructured`

        - **ar_ye** — **text:** `Arabic (Yemen)` · **value:** `ar_ye` · **primaryType:** `nt:unstructured`

        - **be_by** — **text:** `Belorussian (Belorussia)` · **value:** `be_by` · **primaryType:** `nt:unstructured`

        - **bg_bg** — **text:** `Bulgarian (Bulgaria)` · **value:** `bg_bg` · **primaryType:** `nt:unstructured`

        - **ca_es** — **text:** `Catalan (Spain)` · **value:** `ca_es` · **primaryType:** `nt:unstructured`

        - **cs_cz** — **text:** `Czech (Czech Republic)` · **value:** `cs_cz` · **primaryType:** `nt:unstructured`

        - **da_dk** — **text:** `Danish (Denmark)` · **value:** `da_dk` · **primaryType:** `nt:unstructured`

        - **de** — **text:** `German` · **value:** `de` · **primaryType:** `nt:unstructured`

        - **de_at** — **text:** `German (Austria)` · **value:** `de_at` · **primaryType:** `nt:unstructured`

        - **de_ch** — **text:** `German (Switzerland)` · **value:** `de_ch` · **primaryType:** `nt:unstructured`

        - **de_de** — **text:** `German (Germany)` · **value:** `de_de` · **primaryType:** `nt:unstructured`

        - **de_lu** — **text:** `German (Luxembourg)` · **value:** `de_lu` · **primaryType:** `nt:unstructured`

        - **el_gr** — **text:** `Greek (Greece)` · **value:** `el_gr` · **primaryType:** `nt:unstructured`

        - **en** — **text:** `English` · **value:** `en` · **primaryType:** `nt:unstructured`

        - **en_au** — **text:** `English (Australia)` · **value:** `en_au` · **primaryType:** `nt:unstructured`

        - **en_ca** — **text:** `English (Canada)` · **value:** `en_ca` · **primaryType:** `nt:unstructured`

        - **en_gb** — **text:** `English (United Kingdom)` · **value:** `en_gb` · **primaryType:** `nt:unstructured`

        - **en_ie** — **text:** `English (Ireland)` · **value:** `en_ie` · **primaryType:** `nt:unstructured`

        - **en_in** — **text:** `English (India)` · **value:** `en_in` · **primaryType:** `nt:unstructured`

        - **en_nz** — **text:** `English (New Zealand)` · **value:** `en_nz` · **primaryType:** `nt:unstructured`

        - **en_us** — **text:** `English (United States)` · **value:** `en_us` · **primaryType:** `nt:unstructured`

        - **en_za** — **text:** `English (South Africa)` · **value:** `en_za` · **primaryType:** `nt:unstructured`

        - **es** — **text:** `Spanish` · **value:** `es` · **primaryType:** `nt:unstructured`

        - **es_ar** — **text:** `Spanish (Argentina)` · **value:** `es_ar` · **primaryType:** `nt:unstructured`

        - **es_bo** — **text:** `Spanish (Bolivia)` · **value:** `es_bo` · **primaryType:** `nt:unstructured`

        - **es_cl** — **text:** `Spanish (Chile)` · **value:** `es_cl` · **primaryType:** `nt:unstructured`

        - **es_co** — **text:** `Spanish (Colombia)` · **value:** `es_co` · **primaryType:** `nt:unstructured`

        - **es_cr** — **text:** `Spanish (Costa Rica)` · **value:** `es_cr` · **primaryType:** `nt:unstructured`

        - **es_do** — **text:** `Spanish (Dominican Republic)` · **value:** `es_do` · **primaryType:** `nt:unstructured`

        - **es_ec** — **text:** `Spanish (Ecuador)` · **value:** `es_ec` · **primaryType:** `nt:unstructured`

        - **es_es** — **text:** `Spanish (Spain)` · **value:** `es_es` · **primaryType:** `nt:unstructured`

        - **es_gt** — **text:** `Spanish (Guatemala)` · **value:** `es_gt` · **primaryType:** `nt:unstructured`

        - **es_hn** — **text:** `Spanish (Honduras)` · **value:** `es_hn` · **primaryType:** `nt:unstructured`

        - **es_mx** — **text:** `Spanish (Mexico)` · **value:** `es_mx` · **primaryType:** `nt:unstructured`

        - **es_ni** — **text:** `Spanish (Nicaragua)` · **value:** `es_ni` · **primaryType:** `nt:unstructured`

        - **es_pa** — **text:** `Spanish (Panama)` · **value:** `es_pa` · **primaryType:** `nt:unstructured`

        - **es_pe** — **text:** `Spanish (Peru)` · **value:** `es_pe` · **primaryType:** `nt:unstructured`

        - **es_pr** — **text:** `Spanish (Puerto Rico)` · **value:** `es_pr` · **primaryType:** `nt:unstructured`

        - **es_py** — **text:** `Spanish (Paraguay)` · **value:** `es_py` · **primaryType:** `nt:unstructured`

        - **es_sv** — **text:** `Spanish (El Salvador)` · **value:** `es_sv` · **primaryType:** `nt:unstructured`

        - **es_uy** — **text:** `Spanish (Uruguay)` · **value:** `es_uy` · **primaryType:** `nt:unstructured`

        - **es_ve** — **text:** `Spanish (Venezuela)` · **value:** `es_ve` · **primaryType:** `nt:unstructured`

        - **et_ee** — **text:** `Estonian (Estonia)` · **value:** `et_ee` · **primaryType:** `nt:unstructured`

        - **fi_fi** — **text:** `Finnish (Finland)` · **value:** `fi_fi` · **primaryType:** `nt:unstructured`

        - **fr** — **text:** `French` · **value:** `fr` · **primaryType:** `nt:unstructured`

        - **fr_be** — **text:** `French (Belgium)` · **value:** `fr_be` · **primaryType:** `nt:unstructured`

        - **fr_ca** — **text:** `French (Canada)` · **value:** `fr_ca` · **primaryType:** `nt:unstructured`

        - **fr_ch** — **text:** `French (Switzerland)` · **value:** `fr_ch` · **primaryType:** `nt:unstructured`

        - **fr_fr** — **text:** `French (France)` · **value:** `fr_fr` · **primaryType:** `nt:unstructured`

        - **fr_lu** — **text:** `French (Luxembourg)` · **value:** `fr_lu` · **primaryType:** `nt:unstructured`

        - **hi_in** — **text:** `Hindi (India)` · **value:** `hi_in` · **primaryType:** `nt:unstructured`

        - **hr_hr** — **text:** `Croatian (Croatia)` · **value:** `hr_hr` · **primaryType:** `nt:unstructured`

        - **hu_hu** — **text:** `Hungarian (Hungary)` · **value:** `hu_hu` · **primaryType:** `nt:unstructured`

        - **is_is** — **text:** `Icelandic (Iceland)` · **value:** `is_is` · **primaryType:** `nt:unstructured`

        - **it** — **text:** `Italian` · **value:** `it` · **primaryType:** `nt:unstructured`

        - **it_ch** — **text:** `Italian (Switzerland)` · **value:** `it_ch` · **primaryType:** `nt:unstructured`

        - **it_it** — **text:** `Italian (Italy)` · **value:** `it_it` · **primaryType:** `nt:unstructured`

        - **iw_il** — **text:** `Hebrew (Israel)` · **value:** `iw_il` · **primaryType:** `nt:unstructured`

        - **ja** — **text:** `Japanese` · **value:** `ja` · **primaryType:** `nt:unstructured`

        - **ja_jp** — **text:** `Japanese (Japan)` · **value:** `ja_jp` · **primaryType:** `nt:unstructured`

        - **ko_kr** — **text:** `Korean (South Korea)` · **value:** `ko_kr` · **primaryType:** `nt:unstructured`

        - **lt_lt** — **text:** `Lithuanian (Lithuania)` · **value:** `lt_lt` · **primaryType:** `nt:unstructured`

        - **lv_lv** — **text:** `Latvian (Latvia)` · **value:** `lv_lv` · **primaryType:** `nt:unstructured`

        - **mk_mk** — **text:** `Macedonian (Macedonia)` · **value:** `mk_mk` · **primaryType:** `nt:unstructured`

        - **nl_be** — **text:** `Dutch (Belgium)` · **value:** `nl_be` · **primaryType:** `nt:unstructured`

        - **nl_nl** — **text:** `Dutch (Netherlands)` · **value:** `nl_nl` · **primaryType:** `nt:unstructured`

        - **no_no** — **text:** `Norwegian (Bokmål) (Norway)` · **value:** `no_no` · **primaryType:** `nt:unstructured`

        - **no_no_ny** — **text:** `Norwegian (Nynorsk) (Norway)` · **value:** `no_no_ny` · **primaryType:** `nt:unstructured`

        - **pl_pl** — **text:** `Polish (Poland)` · **value:** `pl_pl` · **primaryType:** `nt:unstructured`

        - **pt** — **text:** `Portuguese` · **value:** `pt` · **primaryType:** `nt:unstructured`

        - **pt_br** — **text:** `Portuguese (Brazil)` · **value:** `pt_br` · **primaryType:** `nt:unstructured`

        - **pt_pt** — **text:** `Portuguese (Portugal)` · **value:** `pt_pt` · **primaryType:** `nt:unstructured`

        - **ro_ro** — **text:** `Romanian (Romania)` · **value:** `ro_ro` · **primaryType:** `nt:unstructured`

        - **ru** — **text:** `Russian` · **value:** `ru` · **primaryType:** `nt:unstructured`

        - **ru_ru** — **text:** `Russian (Russia)` · **value:** `ru_ru` · **primaryType:** `nt:unstructured`

        - **sh_yu** — **text:** `Serbo-Croatian (Yugoslavia)` · **value:** `sh_yu` · **primaryType:** `nt:unstructured`

        - **sk_sk** — **text:** `Slovak (Slovakia)` · **value:** `sk_sk` · **primaryType:** `nt:unstructured`

        - **sl_si** — **text:** `Slovenian (Slovenia)` · **value:** `sl_si` · **primaryType:** `nt:unstructured`

        - **sq_al** — **text:** `Albanian (Albania)` · **value:** `sq_al` · **primaryType:** `nt:unstructured`

        - **sr_yu** — **text:** `Serbian (Cyrillic) (Yugoslavia)` · **value:** `sr_yu` · **primaryType:** `nt:unstructured`

        - **sv** — **text:** `Swedish` · **value:** `sv` · **primaryType:** `nt:unstructured`

        - **sv_se** — **text:** `Swedish (Sweden)` · **value:** `sv_se` · **primaryType:** `nt:unstructured`

        - **th_th** — **text:** `Thai (Western digits) (Thailand)` · **value:** `th_th` · **primaryType:** `nt:unstructured`

        - **th_th_th** — **text:** `Thai (Thai digits) (Thailand)` · **value:** `th_th_th` · **primaryType:** `nt:unstructured`

        - **tr_tr** — **text:** `Turkish (Turkey)` · **value:** `tr_tr` · **primaryType:** `nt:unstructured`

        - **uk_ua** — **text:** `Ukrainian (Ukraine)` · **value:** `uk_ua` · **primaryType:** `nt:unstructured`

        - **zh** — **text:** `Chinese (Simplified)` · **value:** `zh` · **primaryType:** `nt:unstructured`

        - **zh_cn** — **text:** `Simplified Chinese (China)` · **value:** `zh_cn` · **primaryType:** `nt:unstructured`

        - **zh_hk** — **text:** `Chinese (Hong Kong SAR of China)` · **value:** `zh_hk` · **primaryType:** `nt:unstructured`

        - **zh_tw** — **text:** `Chinese (Taiwan region)` · **value:** `zh_tw` · **primaryType:** `nt:unstructured`

      - **cascadeitems** — **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/cascadeitems` · **primaryType:** `nt:unstructured`

    - **tags** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Tags` · **metaType:** `tags` · **name:** `./jcr:content/metadata/cq:tags` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/cq:tags` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **colortags** — **fieldLabel:** `Smart Color Tags` · **metaType:** `colortags` · **resourceType:** `dam/gui/coral/components/admin/colortags` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **rendercondition** — **resourceType:** `dam/gui/coral/components/commons/renderconditions/showcolortags` · **primaryType:** `nt:unstructured`

    - **autotags** — **fieldLabel:** `Smart Tags` · **metaType:** `autotags` · **name:** `./jcr:content/metadata/predictedTags` · **readOnly:** `{Boolean}true` · **resourceType:** `dam/gui/coral/components/admin/autotag` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **rendercondition** — **resourceType:** `dam/gui/coral/components/admin/autotag/autotagrendercondition` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/predictedTags` · **primaryType:** `nt:unstructured`

    - **creation** — **fieldLabel:** `Created` · **name:** `./jcr:created` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/datepicker` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./jcr:created` · **metaType:** `datepicker` · **requiredCascading:** `default` · **typeHint:** `Date` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **creatortool** — **fieldLabel:** `Creator Tool` · **name:** `./jcr:content/metadata/xmp:CreatorTool` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/xmp:CreatorTool` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **reviewstatus** — **emptyText:** `Select Option` · **fieldLabel:** `Review Status` · **name:** `./jcr:content/metadata/dam:status` · **readOnly:** `{Boolean}true` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/formfields/v2/metadataselect` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **choicesCascading:** `default` · **cq-msm-lockable:** `./metadata/dam:status` · **metaType:** `dropdown` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **approved** — **text:** `Approved` · **value:** `approved` · **primaryType:** `nt:unstructured`

        - **rejected** — **text:** `Rejected` · **value:** `rejected` · **primaryType:** `nt:unstructured`

        - **changesrequested** — **text:** `Changes Requested` · **value:** `changesRequested` · **primaryType:** `nt:unstructured`

      - **cascadeitems** — **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/cascadeitems` · **primaryType:** `nt:unstructured`

- **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Scheduled (de)activation` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **ontime** — **fieldLabel:** `On Time (MM-DD-YYYY HH:mm)` · **name:** `./jcr:content/onTime` · **resourceType:** `granite/ui/components/coral/foundation/form/datepicker` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./onTime` · **metaType:** `datepicker` · **requiredCascading:** `default` · **typeHint:** `Date` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **offime** — **fieldLabel:** `Off Time (MM-DD-YYYY HH:mm)` · **name:** `./jcr:content/offTime` · **resourceType:** `granite/ui/components/coral/foundation/form/datepicker` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./offTime` · **metaType:** `datepicker` · **requiredCascading:** `default` · **typeHint:** `Date` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Seminole Hard Rock Support Services` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **brands** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Brand` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrssbrands` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrssbrands` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **venues** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Venues & Branded Experiences ` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrssvenues` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrssvenues` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **lob** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Line of Business` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrsslob` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrsslob` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **property** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Property Names (Locators / City Drop)` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrssproperty` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrssproperty` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **type** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Type` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrsstype` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrsstype` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **category** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Category` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrsscategory` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrsscategory` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **product** — **cq-msm-lockable:** `cq:tags` · **fieldLabel:** `Product` · **metaType:** `tags` · **name:** `./jcr:content/metadata/shrssproduct` · **resourceType:** `cq/gui/components/coral/common/form/tagfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/shrssproduct` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **altText** — **fieldLabel:** `(Alternative  Text )altText` · **name:** `./jcr:content/metadata/altText` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/altText` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col4** — **listOrder:** `3` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header1** — **fieldLabel:** `Compositions` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **referencing** — **fieldLabel:** `Dependencies` · **resourceType:** `dam/gui/components/admin/referencing` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `referencing` · **primaryType:** `nt:unstructured`

    - **header2** — **fieldLabel:** `Related` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **source** — **fieldLabel:** `Source` · **resourceType:** `dam/gui/components/admin/relation` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `sources` · **primaryType:** `nt:unstructured`

    - **derived** — **fieldLabel:** `Derived` · **resourceType:** `dam/gui/components/admin/relation` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `derived` · **primaryType:** `nt:unstructured`

    - **others** — **fieldLabel:** `Others` · **resourceType:** `dam/gui/components/admin/relation` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `others` · **primaryType:** `nt:unstructured`

    - **header3** — **fieldLabel:** `Subassets` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

##### tab2

**listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Advanced`

###### data

**tabid:** `7c927721-1473-492f-b949-4fa2f82a32a0` · **primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `License` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **creator** — **fieldLabel:** `Creator` · **name:** `./jcr:content/metadata/dc:creator` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:creator` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **contributor** — **fieldLabel:** `Contributor` · **name:** `./jcr:content/metadata/dc:contributor` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:contributor` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **copyright** — **fieldLabel:** `Copyright` · **name:** `./jcr:content/metadata/dc:rights` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/dc:rights` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **copyrightowner** — **fieldLabel:** `Copyright Owner` · **name:** `./jcr:content/metadata/xmpRights:Owner` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/xmpRights:Owner` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **usageterms** — **fieldLabel:** `Usage Terms` · **name:** `./jcr:content/metadata/xmpRights:UsageTerms` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/xmpRights:UsageTerms` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **expires** — **fieldLabel:** `Expires (MM-DD-YYYY HH:mm)` · **name:** `./jcr:content/metadata/prism:expirationDate` · **resourceType:** `granite/ui/components/coral/foundation/form/datepicker` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/prism:expirationDate` · **metaType:** `datepicker` · **requiredCascading:** `default` · **typeHint:** `Date` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **id** — **fieldLabel:** `ID` · **name:** `./jcr:uuid` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./jcr:uuid` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Creative Rating` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **creativerating** — **fieldLabel:** `Rating` · **name:** `./jcr:content/metadata/xmp:Rating` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/numberfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/xmp:Rating` · **metaType:** `number` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **rating** — **fieldLabel:** `Rating` · **resourceType:** `dam/gui/coral/components/admin/rating` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `assetrating` · **primaryType:** `nt:unstructured`

- **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

- **col4** — **listOrder:** `3` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Elevate for search keywords` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **search_promote** — **fieldLabel:** `Search Promote` · **resourceType:** `granite/ui/components/coral/foundation/form/multifield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `mvtext` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **field** — **name:** `./jcr:content/metadata/dam:search_promote` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/dam:search_promote` · **primaryType:** `nt:unstructured`

##### tab3

**listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `IPTC`

###### data

**primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Contact` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **creatorjobtitle** — **fieldLabel:** `Creator's Job Title` · **name:** `./jcr:content/metadata/photoshop:AuthorsPosition` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:AuthorsPosition` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **address** — **fieldLabel:** `Address` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **city** — **fieldLabel:** `City` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrCity` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **state** — **fieldLabel:** `State/Province` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrRegion` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **postalcode** — **fieldLabel:** `Postal Code` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrPcode` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **country** — **fieldLabel:** `Country` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrCtry` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **phone** — **fieldLabel:** `Phone(s)` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiTelWork` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **email** — **fieldLabel:** `E-Mail(s)` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiEmailWork` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **website** — **fieldLabel:** `Website(s)` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiUrlWork` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Image` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **datecreated** — **fieldLabel:** `Date Created (YYYY-MM-DD HH:mm)` · **name:** `./jcr:content/metadata/photoshop:DateCreated` · **resourceType:** `granite/ui/components/coral/foundation/form/datepicker` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:DateCreated` · **metaType:** `datepicker` · **requiredCascading:** `default` · **typeHint:** `Date` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **genre** — **fieldLabel:** `Intellectual Genre` · **name:** `./jcr:content/metadata/Iptc4xmpCore:IntellectualGenre` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:IntellectualGenre` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **scenecode** — **emptyText:** `Select Option` · **fieldLabel:** `IPTC Scene Code` · **name:** `./jcr:content/metadata/Iptc4xmpCore:Scene` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/formfields/v2/metadataselect` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **choicesCascading:** `default` · **cq-msm-lockable:** `./metadata/Iptc4xmpCore:Scene` · **metaType:** `dropdown` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **items** — **primaryType:** `nt:unstructured`

        - **_x0030_10100** — **text:** `headshot` · **value:** `scn:010100` · **primaryType:** `nt:unstructured`

        - **_x0030_10200** — **text:** `half-length` · **value:** `scn:010200` · **primaryType:** `nt:unstructured`

        - **_x0030_10300** — **text:** `full-length` · **value:** `scn:010300` · **primaryType:** `nt:unstructured`

        - **_x0030_10400** — **text:** `profile` · **value:** `scn:010400` · **primaryType:** `nt:unstructured`

        - **_x0030_10500** — **text:** `rear view` · **value:** `scn:010500` · **primaryType:** `nt:unstructured`

        - **_x0030_10600** — **text:** `single` · **value:** `scn:010600` · **primaryType:** `nt:unstructured`

        - **_x0030_10700** — **text:** `couple` · **value:** `scn:010700,` · **primaryType:** `nt:unstructured`

        - **_x0030_10800** — **text:** `two` · **value:** `scn:010800` · **primaryType:** `nt:unstructured`

        - **_x0030_10900** — **text:** `group` · **value:** `scn:010900` · **primaryType:** `nt:unstructured`

        - **_x0030_11000** — **text:** `general view` · **value:** `scn:011000` · **primaryType:** `nt:unstructured`

        - **_x0030_11100** — **text:** `panoramic view` · **value:** `scn:011100` · **primaryType:** `nt:unstructured`

        - **_x0030_11200** — **text:** `aerial view` · **value:** `scn:011200` · **primaryType:** `nt:unstructured`

        - **_x0030_11300** — **text:** `scn:011300` · **value:** `under-water` · **primaryType:** `nt:unstructured`

        - **_x0030_11400** — **text:** `night scene` · **value:** `scn:011400` · **primaryType:** `nt:unstructured`

        - **_x0030_11500** — **text:** `satellite` · **value:** `scn:011500` · **primaryType:** `nt:unstructured`

        - **_x0030_11600** — **text:** `exterior view` · **value:** `scn:011600` · **primaryType:** `nt:unstructured`

        - **_x0030_11700** — **text:** `interior view` · **value:** `scn:011700` · **primaryType:** `nt:unstructured`

        - **_x0030_11800** — **text:** `close-up` · **value:** `scn:011800` · **primaryType:** `nt:unstructured`

        - **_x0030_11900** — **text:** `action` · **value:** `scn:011900` · **primaryType:** `nt:unstructured`

        - **_x0030_12000** — **text:** `performing` · **value:** `scn:012000` · **primaryType:** `nt:unstructured`

        - **_x0030_12100** — **text:** `posing` · **value:** `scn:012100` · **primaryType:** `nt:unstructured`

        - **_x0030_12200** — **text:** `symbolic` · **value:** `scn:012200` · **primaryType:** `nt:unstructured`

        - **_x0030_12300** — **text:** `off-beat` · **value:** `scn:012300` · **primaryType:** `nt:unstructured`

        - **_x0030_12400** — **text:** `movie scene` · **value:** `scn:012400` · **primaryType:** `nt:unstructured`

      - **cascadeitems** — **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/cascadeitems` · **primaryType:** `nt:unstructured`

    - **sublocation** — **fieldLabel:** `Sublocation` · **name:** `./jcr:content/metadata/Iptc4xmpCore:Location` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:Location` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **imagecity** — **fieldLabel:** `City` · **name:** `./jcr:content/metadata/photoshop:City` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:City` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **imagestate** — **fieldLabel:** `State/Province` · **name:** `./jcr:content/metadata/photoshop:State` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:State` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **imagecountry** — **fieldLabel:** `Country` · **name:** `./jcr:content/metadata/photoshop:Country` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:Country` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **isocountrycode** — **fieldLabel:** `ISO Country Code` · **name:** `./jcr:content/metadata/Iptc4xmpCore:CountryCode` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:CountryCode` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **alttextaccessibility** — **fieldLabel:** `Alt Text` · **name:** `./jcr:content/metadata/Iptc4xmpCore:AltTextAccessibility` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:AltTextAccessibility` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **extdescraccessibility** — **fieldLabel:** `Extended Description` · **name:** `./jcr:content/metadata/Iptc4xmpCore:ExtDescrAccessibility` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:ExtDescrAccessibility` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Content and Status` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **headline** — **fieldLabel:** `Headline` · **name:** `./jcr:content/metadata/photoshop:Headline` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:Headline` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **keywords** — **fieldLabel:** `Keywords` · **resourceType:** `granite/ui/components/coral/foundation/form/multifield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `mvtext` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **field** — **name:** `./jcr:content/metadata/dc:subject` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/dc:subject` · **primaryType:** `nt:unstructured`

    - **subjectcode** — **fieldLabel:** `IPTC Subject Code` · **name:** `./jcr:content/metadata/Iptc4xmpCore:SubjectCode` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpCore:SubjectCode` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **writerdescription** — **fieldLabel:** `Description Writer` · **name:** `./jcr:content/metadata/photoshop:CaptionWriter` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:CaptionWriter` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **jobidentifier** — **fieldLabel:** `Job Identifier` · **name:** `./jcr:content/metadata/photoshop:TransmissionReference` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:TransmissionReference` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **instructions** — **fieldLabel:** `Instructions` · **name:** `./jcr:content/metadata/photoshop:Instructions` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:Instructions` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **creditline** — **fieldLabel:** `Credit Line` · **name:** `./jcr:content/metadata/photoshop:Credit` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:Credit` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **source** — **fieldLabel:** `Source` · **name:** `./jcr:content/metadata/photoshop:Source` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/photoshop:Source` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

##### tab4

**listOrder:** `3` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `IPTC Extension`

###### data

**primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Description of Image` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **personshown** — **fieldLabel:** `Person  Shown` · **resourceType:** `granite/ui/components/coral/foundation/form/multifield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `mvtext` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

      - **field** — **name:** `./jcr:content/metadata/Iptc4xmpExt:PersonInImage` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **primaryType:** `nt:unstructured`

        - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:PersonInImage` · **primaryType:** `nt:unstructured`

    - **organisationimagename** — **fieldLabel:** `Name of Featured Organisation` · **name:** `./jcr:content/metadata/Iptc4xmpExt:OrganisationInImageName` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:OrganisationInImageName` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **organisationimagecode** — **fieldLabel:** `Code of Featured Organisation` · **name:** `./jcr:content/metadata/Iptc4xmpExt:OrganisationInImageCode` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:OrganisationInImageCode` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `About Models in Image` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **modelinfo** — **fieldLabel:** `Additional Model Info` · **name:** `./jcr:content/metadata/Iptc4xmpExt:AddlModelInfo` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:AddlModelInfo` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **modelage** — **fieldLabel:** `Model Age` · **name:** `./jcr:content/metadata/Iptc4xmpExt:ModelAge` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:ModelAge` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **modeldisclosure** — **fieldLabel:** `Minor Model Image Disclosure` · **name:** `./jcr:content/metadata/plus:MinorModelAgeDisclosure` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:MinorModelAgeDisclosure` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **modelreleasestatus** — **fieldLabel:** `Model Release Status` · **name:** `./jcr:content/metadata/plus:ModelReleaseStatus` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:ModelReleaseStatus` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **modelreleaseidentifier** — **fieldLabel:** `Model Release Identifier` · **name:** `./jcr:content/metadata/plus:ModelReleaseID` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:ModelReleaseID` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col3** — **listOrder:** `2` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Administrative and Rights Information` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **supplierid** — **fieldLabel:** `Supplier's Image ID` · **name:** `./jcr:content/metadata/plus:ImageSupplierImageID` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:ImageSupplierImageID` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **maxavailwidth** — **fieldLabel:** `Max available Width` · **name:** `./jcr:content/metadata/Iptc4xmpExt:MaxAvailWidth` · **resourceType:** `granite/ui/components/coral/foundation/form/numberfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:MaxAvailWidth` · **metaType:** `number` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **maxavailheight** — **fieldLabel:** `Max. available Height` · **name:** `./jcr:content/metadata/Iptc4xmpExt:MaxAvailHeight` · **resourceType:** `granite/ui/components/coral/foundation/form/numberfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:MaxAvailHeight` · **metaType:** `number` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **digitalsourcetype** — **fieldLabel:** `Digital Source Type` · **name:** `./jcr:content/metadata/Iptc4xmpExt:DigitalSourceType` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/Iptc4xmpExt:DigitalSourceType` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **propertyreleasestatus** — **fieldLabel:** `Property Release Status` · **name:** `./jcr:content/metadata/plus:PropertyReleaseStatus` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:PropertyReleaseStatus` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **propertyreleaseid** — **fieldLabel:** `Property Release Identifier` · **name:** `./jcr:content/metadata/plus:PropertyReleaseID` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/plus:PropertyReleaseID` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

##### tab5

**listOrder:** `4` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-tab` · **primaryType:** `nt:unstructured` · **title:** `Camera Data`

###### data

**primaryType:** `nt:unstructured`

###### items

**primaryType:** `nt:unstructured`

- **col1** — **listOrder:** `0` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Camera Information test` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **make** — **fieldLabel:** `Make` · **name:** `./jcr:content/metadata/tiff:Make` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/tiff:Make` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **model** — **fieldLabel:** `Model` · **name:** `./jcr:content/metadata/tiff:Model` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/tiff:Model` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **owner** — **fieldLabel:** `Owner` · **name:** `./jcr:content/metadata/psAux:OwnerName` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/psAux:OwnerName` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **lens** — **fieldLabel:** `Lens` · **name:** `./jcr:content/metadata/psAux:Lens` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/psAux:Lens` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

- **col2** — **listOrder:** `1` · **resourceType:** `granite/ui/components/coral/foundation/container` · **rel:** `aem-assets-metadata-form-column` · **primaryType:** `nt:unstructured`

  - **items** — **primaryType:** `nt:unstructured`

    - **header** — **fieldLabel:** `Shot Information` · **resourceType:** `dam/gui/coral/components/admin/schemaforms/formbuilder/sectionfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `section` · **primaryType:** `nt:unstructured`

    - **focallength** — **fieldLabel:** `Focal Length (in mm)` · **name:** `./jcr:content/metadata/exif:FocalLength` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/exif:FocalLength` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **focallength35mm** — **fieldLabel:** `Focal Length (in 35 mm)` · **name:** `./jcr:content/metadata/exif:FocalLengthIn35mmFilm` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/exif:FocalLengthIn35mmFilm` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **exposure** — **fieldLabel:** `Exposure Time (secs)` · **name:** `./jcr:content/metadata/exif:ExposureTime` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/exif:ExposureTime` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **fnumber** — **fieldLabel:** `F-Number` · **name:** `./jcr:content/metadata/exif:FNumber` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/exif:FNumber` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **iso** — **fieldLabel:** `ISO` · **name:** `./jcr:content/metadata/exifEX:PhotographicSensitivity` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/exifEX:PhotographicSensitivity` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **orientation** — **fieldLabel:** `Orientation` · **name:** `./jcr:content/metadata/tiff:Orientation` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/tiff:Orientation` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **resolution** — **fieldLabel:** `Resolution (Pixels per Inch)` · **name:** `./jcr:content/metadata/tiff:XResolution` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **cq-msm-lockable:** `./metadata/tiff:XResolution` · **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`

    - **flash** — **fieldLabel:** `Flash` · **name:** `./jcr:content/metadata/exif:Flash/exif:Fired` · **readOnly:** `{Boolean}true` · **resourceType:** `granite/ui/components/coral/foundation/form/textfield` · **resourceType:** `dam/gui/components/admin/schemafield` · **primaryType:** `nt:unstructured`

      - **data** — **metaType:** `text` · **requiredCascading:** `default` · **visibilityCascading:** `default` · **primaryType:** `nt:unstructured`
