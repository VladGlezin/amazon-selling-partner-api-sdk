# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_ids** | **list[str]** | A list of marketplace identifiers for the report. | [optional] 
**report_id** | **str** | The identifier for the report. This identifier is unique only in combination with a seller ID. | 
**report_type** | **str** | The report type. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information. | 
**data_start_time** | **datetime** | The start of a date and time range used for selecting the data to report. | [optional] 
**data_end_time** | **datetime** | The end of a date and time range used for selecting the data to report. | [optional] 
**report_schedule_id** | **str** | The identifier of the report schedule that created this report (if any). This identifier is unique only in combination with a seller ID. | [optional] 
**created_time** | **datetime** | The date and time when the report was created. | 
**processing_status** | **str** | The processing status of the report. | 
**processing_start_time** | **datetime** | The date and time when the report processing started, in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; date time format. | [optional] 
**processing_end_time** | **datetime** | The date and time when the report processing completed, in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; date time format. | [optional] 
**report_document_id** | **str** | The identifier for the report document. Pass this into the &#x60;getReportDocument&#x60; operation to get the information you will need to retrieve the report document&#39;s contents. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

