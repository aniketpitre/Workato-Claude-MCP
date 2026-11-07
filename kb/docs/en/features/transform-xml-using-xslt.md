---
url: 'https://docs.workato.com/en/features/transform-xml-using-xslt.md'
description: >-
  This action applies an XSLT script to transform XML into another format.
  Supports XSLT 1.1 and earlier.
---

# XML tools by Workato - Transform XML using XSLT action

The **Transform XML using XSLT** action applies an XSLT (Extensible Stylesheet Language Transformations) script to an XML document and converts it into a different format, such as another XML structure, HTML, or plain text. This action fully supports XSLT 1.0 and offers partial support for XSLT 2.0. You can define the XSLT script inline or using a [resource](/en/resources).

## Input

| Input field | Description |
| --- | --- |
| XML Document | Provide the XML document to transform. |
| Encoding of the file content | Specify the encoding format for the XML document. If left blank, Workato defaults to **UTF-8**. |
| XSLT Document | Select **Define manually** to provide XSLT inline, or **Use a resource** to use a resource as the XSLT stylesheet. |
| XSLT Resource | Select the resource to use as the stylesheet. This field appears when you select **Use a resource** in the **XSLT Document** drop-down menu. |
| XSLT Contents | Provide the XSLT script that defines how to transform the XML document. Ensure that any imports or includes don't contain absolute paths. For example, `imported.xsl`. This field appears when you select **Define manually** in the **XSLT Document** drop-down menu. |
| XSLT references | Provide the names and contents of up to five referenced stylesheets if the XSLT script includes imports or includes. This field appears when you select **Define manually** in the **XSLT Document** drop-down menu. |
| XSLT parameters | Specify the names and values if the XSLT script includes parameters. |
| Response content type | Select the expected format of the transformed output. Choose **Raw text response body** to return unstructured text, or choose **Structured response** to generate datapills based on a sample document. If the transformation output does not match the selected format, the action fails. |
| Response body example | Provide a sample document that represents the expected output structure if **Structured response** is selected as the **Response content type**. Workato uses this sample to generate datapills. If left blank, the action returns a single raw output datapill. |

## Output

Workato returns the raw transformation output if you select **Raw text response body**. Workato generates datapills based on the sample document provided if you select **Structured response**.

## Sample use case

An XSLT script defines how Workato should transform an XML document. The following XSLT script converts raw XML data into a structured format:

Sample XSLT

```xml
<xsl:stylesheet xsl:version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:key name="groups" match="/holder/segment[field[1]='PO1' or field[1]='PID' or field[1]='PO4']" use="generate-id(preceding-sibling::segment[field[1]='PO1'][1])" />
	<xsl:template match="/">
		<EDI850>
			<ISA>
				<AuthorizationInformationQualifier>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[2]"/>
				</AuthorizationInformationQualifier>
				<AuthorizationInformation>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[3]"/>
				</AuthorizationInformation>
				<SecurityInformationQualifier>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[4]"/>
				</SecurityInformationQualifier>
				<SecurityInformation>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[5]"/>
				</SecurityInformation>
				<InterchangeIdQualifier_Sender>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[6]"/>
				</InterchangeIdQualifier_Sender>
				<InterchangeSenderId>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[7]"/>
				</InterchangeSenderId>
				<InterchangeIdQualifier_Receiver>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[8]"/>
				</InterchangeIdQualifier_Receiver>
				<InterchangeReceiverId>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[9]"/>
				</InterchangeReceiverId>
				<InterchangeDate>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[10]"/>
				</InterchangeDate>
				<InterchangeTime>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[11]"/>
				</InterchangeTime>
				<InterchangeControlVersion>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[12]"/>
				</InterchangeControlVersion>
				<InterchangeControlStandardsIdentifier>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[13]"/>
				</InterchangeControlStandardsIdentifier>
				<InterchangeControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[14]"/>
				</InterchangeControlNumber>
				<AcknowledgementRequested>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[15]"/>
				</AcknowledgementRequested>
				<UsageIndicator>
					<xsl:value-of select="/holder/segment[field[1] = 'ISA']/field[16]"/>
				</UsageIndicator>
			</ISA>
			<GS>
				<FunctionalIdentifierCode>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[2]"/>
				</FunctionalIdentifierCode>
				<ApplicationSenderCode>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[3]"/>
				</ApplicationSenderCode>
				<ApplicationReceiverCode>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[4]"/>
				</ApplicationReceiverCode>
				<Date>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[5]"/>
				</Date>
				<Time>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[6]"/>
				</Time>
				<GroupControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[7]"/>
				</GroupControlNumber>
				<ResponsibleAgencyCode>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[8]"/>
				</ResponsibleAgencyCode>
				<VersionReleaseIndustryIdentifierCode>
					<xsl:value-of select="/holder/segment[field[1] = 'GS']/field[9]"/>
				</VersionReleaseIndustryIdentifierCode>
			</GS>
			<ST>
				<TransactionSetIdentifierCode>
					<xsl:value-of select="/holder/segment[field[1] = 'ST']/field[2]"/>
				</TransactionSetIdentifierCode>
				<TransactionSetControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'ST']/field[3]"/>
				</TransactionSetControlNumber>
			</ST>
			<BEG>
				<TransactionSetPurposeCode>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[2]"/>
				</TransactionSetPurposeCode>
				<PurchaseOrderTypeCode>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[3]"/>
				</PurchaseOrderTypeCode>
				<PurchaseOrderNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[4]"/>
				</PurchaseOrderNumber>
				<ReleaseNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[5]"/>
				</ReleaseNumber>
				<PurchaseOrderDate>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[6]"/>
				</PurchaseOrderDate>
				<ContactNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'BEG']/field[7]"/>
				</ContactNumber>
			</BEG>
			<ITD>
				<TermsTypeCode>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[2]"/>
				</TermsTypeCode>
				<TermsBasisDateCode>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[3]"/>
				</TermsBasisDateCode>
				<TermsDiscountPercent>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[4]"/>
				</TermsDiscountPercent>
				<TermsDiscountDueDays>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[5]"/>
				</TermsDiscountDueDays>
				<TermsNetDays>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[6]"/>
				</TermsNetDays>
				<Description >
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[7]"/>
				</Description>
				<DayOfMonth>
					<xsl:value-of select="/holder/segment[field[1] = 'ITD']/field[8]"/>
				</DayOfMonth>
			</ITD>
			<DTM>
				<DateTimeQualifier>
					<xsl:value-of select="/holder/segment[field[1] = 'DTM']/field[2]"/>
				</DateTimeQualifier>
				<Date>
					<xsl:value-of select="/holder/segment[field[1] = 'DTM']/field[3]"/>
				</Date>
			</DTM>
			<xsl:for-each select="/holder/segment[field[1] = 'PKG']">
				<PKG>
					<ItemDescriptionType>
						<xsl:value-of select="field[2]"/>
					</ItemDescriptionType>
					<PackagingCharacteristicCode>
						<xsl:value-of select="field[3]"/>
					</PackagingCharacteristicCode>
					<Description>
						<xsl:value-of select="field[4]"/>
					</Description>
				</PKG>
			</xsl:for-each>
			<TD5>
				<RoutingSequenceCode>
					<xsl:value-of select="/holder/segment[field[1] = 'TD5']/field[2]"/>
				</RoutingSequenceCode>
				<IdentificationCodeQualifier>
					<xsl:value-of select="/holder/segment[field[1] = 'TD5']/field[3]"/>
				</IdentificationCodeQualifier>
				<IdentificationCode>
					<xsl:value-of select="/holder/segment[field[1] = 'TD5']/field[4]"/>
				</IdentificationCode>
				<TransportationMethodTypeCode>
					<xsl:value-of select="/holder/segment[field[1] = 'TD5']/field[6]"/>
				</TransportationMethodTypeCode>
			</TD5>
			<N1>
				<EntityIdentifierCode>
					<xsl:value-of select="/holder/segment[field[1] = 'N1']/field[2]"/>
				</EntityIdentifierCode>
				<Name>
					<xsl:value-of select="/holder/segment[field[1] = 'N1']/field[3]"/>
				</Name>
				<IdentificationCodeQualifier>
					<xsl:value-of select="/holder/segment[field[1] = 'N1']/field[4]"/>
				</IdentificationCodeQualifier>
				<IdentificationCode>
					<xsl:value-of select="/holder/segment[field[1] = 'N1']/field[5]"/>
				</IdentificationCode>
			</N1>
			<N3>
				<AddressInformation>
					<xsl:value-of select="/holder/segment[field[1] = 'N3']/field[2]"/>
				</AddressInformation>
			</N3>
			<N4>
				<CityName>
					<xsl:value-of select="/holder/segment[field[1] = 'N4']/field[2]"/>
				</CityName>
				<StateOrProvinceCode>
					<xsl:value-of select="/holder/segment[field[1] = 'N4']/field[3]"/>
				</StateOrProvinceCode>
				<PostalCode>
					<xsl:value-of select="/holder/segment[field[1] = 'N4']/field[4]"/>
				</PostalCode>
			</N4>
			<xsl:for-each select="/holder/segment[field[1] = 'PO1']">
				<xsl:variable name="index" select="index"/>
				<xsl:variable name="followingIndex">
					<xsl:choose>
						<xsl:when test="following-sibling::*[(field[1] = 'PO1')]">
							<xsl:value-of select="following-sibling::*[(field[1] = 'PO1')]/index"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="'300'"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>
				<POGroup>
					<PO1>
						<LineNumber>
							<xsl:value-of select="field[2]"/>
						</LineNumber>
						<Quantity>
							<xsl:value-of select="field[3]"/>
						</Quantity>
						<UnitOfMeasurement>
							<xsl:value-of select="field[4]"/>
						</UnitOfMeasurement>
						<UnitPrice>
							<xsl:value-of select="field[5]"/>
						</UnitPrice>
						<BasisOfUnitPriceCode>
							<xsl:value-of select="field[6]"/>
						</BasisOfUnitPriceCode>
						<ProductServiceId>
							<xsl:value-of select="field[7]"/>
						</ProductServiceId>
					</PO1>
					<xsl:for-each select="/holder/segment[field[1] = 'PID']">
						<xsl:if test="number(index) &gt; number($index) and number(index) &lt; number($followingIndex)">
							<PID>
								<ItemDescriptionType>
									<xsl:value-of select="field[2]"/>
								</ItemDescriptionType>
								<Description>
									<xsl:value-of select="field[6]"/>
								</Description>
							</PID>
						</xsl:if>
					</xsl:for-each>
					<xsl:for-each select="/holder/segment[field[1] = 'PO4']">
						<xsl:if test="number(index) &gt; number($index) and number(index) &lt; number($followingIndex)">
							<PO4>
								<Pack>
									<xsl:value-of select="field[2]"/>
								</Pack>
								<Size>
									<xsl:value-of select="field[3]"/>
								</Size>
								<UOM>
									<xsl:value-of select="field[4]"/>
								</UOM>
								<PackagingCode>
									<xsl:value-of select="field[5]"/>
								</PackagingCode>
								<Weight>
									<xsl:value-of select="field[6]"/>
								</Weight>
								<WeightQualifier>
									<xsl:value-of select="field[7]"/>
								</WeightQualifier>
								<Volume>
									<xsl:value-of select="field[8]"/>
								</Volume>
								<VolumeQualifier>
									<xsl:value-of select="field[9]"/>
								</VolumeQualifier>
							</PO4>
						</xsl:if>
					</xsl:for-each>
				</POGroup>
			</xsl:for-each>
			<CTT>
				<NumberofLineItems>
					<xsl:value-of select="/holder/segment[field[1] = 'CTT']/field[2]"/>
				</NumberofLineItems>
			</CTT>
			<AMT>
				<AmountQualifierCode>
					<xsl:value-of select="/holder/segment[field[1] = 'AMT']/field[2]"/>
				</AmountQualifierCode>
				<MonetaryAmount>
					<xsl:value-of select="/holder/segment[field[1] = 'AMT']/field[3]"/>
				</MonetaryAmount>
			</AMT>
			<SE>
				<NumberOfIncludedSegments>
					<xsl:value-of select="/holder/segment[field[1] = 'SE']/field[2]"/>
				</NumberOfIncludedSegments>
				<TransactionSetControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'SE']/field[3]"/>
				</TransactionSetControlNumber>
			</SE>
			<GE>
				<NumberOfTransactionSetsIncluded>
					<xsl:value-of select="/holder/segment[field[1] = 'GE']/field[2]"/>
				</NumberOfTransactionSetsIncluded>
				<GroupControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'GE']/field[3]"/>
				</GroupControlNumber>
			</GE>
			<IEA>
				<NumberOfIncludedGroups>
					<xsl:value-of select="/holder/segment[field[1] = 'IEA']/field[2]"/>
				</NumberOfIncludedGroups>
				<InterchangeControlNumber>
					<xsl:value-of select="/holder/segment[field[1] = 'IEA']/field[3]"/>
				</InterchangeControlNumber>
			</IEA>
		</EDI850>
	</xsl:template>
</xsl:stylesheet>
```

A transformation requires an XML document as input. The following example XML represents the original data before any modifications:

Source XML document

```xml
<?xml version="1.0" encoding="UTF-8"?>
<holder>
	<segment>
		<index>0</index>
		<field>ISA</field>
		<field>01</field>
		<field>0000000000</field>
		<field>01</field>
		<field>0000000000</field>
		<field>ZZ</field>
		<field>ABCDEFGHIJKLMNO</field>
		<field>ZZ</field>
		<field>123456789012345</field>
		<field>101127</field>
		<field>1719</field>
		<field>U</field>
		<field>00400</field>
		<field>000003438</field>
		<field>0</field>
		<field>P</field>
		<field>></field>
	</segment>
	<segment>
		<index>1</index>
		<field>GS</field>
		<field>PO</field>
		<field>4405197800</field>
		<field>999999999</field>
		<field>20101127</field>
		<field>1719</field>
		<field>1421</field>
		<field>X</field>
		<field>004010VICS</field>
	</segment>
	<segment>
		<index>2</index>
		<field>ST</field>
		<field>850</field>
		<field>000000010</field>
	</segment>
	<segment>
		<index>3</index>
		<field>BEG</field>
		<field>00</field>
		<field>SA</field>
		<field>08292233294</field>
		<field>0null</field>
		<field>20101127</field>
		<field>610385385</field>
	</segment>
	<segment>
		<index>4</index>
		<field>REF</field>
		<field>DP</field>
		<field>038</field>
	</segment>
	<segment>
		<index>5</index>
		<field>REF</field>
		<field>PS</field>
		<field>R</field>
	</segment>
	<segment>
		<index>6</index>
		<field>ITD</field>
		<field>14</field>
		<field>3</field>
		<field>2</field>
		<field>0null</field>
		<field>45</field>
		<field>0null</field>
		<field>46</field>
	</segment>
	<segment>
		<index>7</index>
		<field>DTM</field>
		<field>002</field>
		<field>20101214</field>
	</segment>
	<segment>
		<index>8</index>
		<field>PKG</field>
		<field>F</field>
		<field>68</field>
		<field>0null</field>
		<field>0null</field>
		<field>PALLETIZE SHIPMENT</field>
	</segment>
	<segment>
		<index>9</index>
		<field>PKG</field>
		<field>F</field>
		<field>66</field>
		<field>0null</field>
		<field>0null</field>
		<field>REGULAR</field>
	</segment>
	<segment>
		<index>10</index>
		<field>TD5</field>
		<field>A</field>
		<field>92</field>
		<field>P3</field>
		<field>0null</field>
		<field>SEE XYZ RETAIL ROUTING GUIDE</field>
	</segment>
	<segment>
		<index>11</index>
		<field>N1</field>
		<field>ST</field>
		<field>XYZ RETAIL</field>
		<field>9</field>
		<field>0003947268292</field>
	</segment>
	<segment>
		<index>12</index>
		<field>N3</field>
		<field>31875 SOLON RD</field>
	</segment>
	<segment>
		<index>13</index>
		<field>N4</field>
		<field>SOLON</field>
		<field>OH</field>
		<field>44139</field>
	</segment>
	<segment>
		<index>14</index>
		<field>PO1</field>
		<field>1</field>
		<field>120</field>
		<field>EA</field>
		<field>9.25</field>
		<field>TE</field>
		<field>CB</field>
		<field>065322-117</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>AB3542</field>
	</segment>
	<segment>
		<index>15</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>SMALL WIDGET</field>
	</segment>
	<segment>
		<index>16</index>
		<field>PO4</field>
		<field>4</field>
		<field>4</field>
		<field>EA</field>
		<field>PLT94</field>
		<field>0null</field>
		<field>3</field>
		<field>LR</field>
		<field>15</field>
		<field>CT</field>
	</segment>
	<segment>
		<index>17</index>
		<field>PO1</field>
		<field>2</field>
		<field>220</field>
		<field>EA</field>
		<field>13.79</field>
		<field>TE</field>
		<field>CB</field>
		<field>066850-116</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>RD5322</field>
	</segment>
	<segment>
		<index>18</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>MEDIUM WIDGET</field>
	</segment>
	<segment>
		<index>19</index>
		<field>PO4</field>
		<field>2</field>
		<field>2</field>
		<field>EA</field>
	</segment>
	<segment>
		<index>20</index>
		<field>PO1</field>
		<field>3</field>
		<field>126</field>
		<field>EA</field>
		<field>10.99</field>
		<field>TE</field>
		<field>CB</field>
		<field>060733-110</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>XY5266</field>
	</segment>
	<segment>
		<index>21</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>LARGE WIDGET</field>
	</segment>
	<segment>
		<index>22</index>
		<field>PO4</field>
		<field>6</field>
		<field>1</field>
		<field>EA</field>
		<field>PLT94</field>
		<field>0null</field>
		<field>3</field>
		<field>LR</field>
		<field>12</field>
		<field>CT</field>
	</segment>
	<segment>
		<index>23</index>
		<field>PO1</field>
		<field>4</field>
		<field>76</field>
		<field>EA</field>
		<field>4.35</field>
		<field>TE</field>
		<field>CB</field>
		<field>065308-116</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>VX2332</field>
	</segment>
	<segment>
		<index>24</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>NANO WIDGET</field>
	</segment>
	<segment>
		<index>25</index>
		<field>PO4</field>
		<field>4</field>
		<field>4</field>
		<field>EA</field>
		<field>PLT94</field>
		<field>0null</field>
		<field>6</field>
		<field>LR</field>
		<field>19</field>
		<field>CT</field>
	</segment>
	<segment>
		<index>26</index>
		<field>PO1</field>
		<field>5</field>
		<field>72</field>
		<field>EA</field>
		<field>7.5</field>
		<field>TE</field>
		<field>CB</field>
		<field>065374-118</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>RV0524</field>
	</segment>
	<segment>
		<index>27</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>BLUE WIDGET</field>
	</segment>
	<segment>
		<index>28</index>
		<field>PO4</field>
		<field>4</field>
		<field>4</field>
		<field>EA</field>
	</segment>
	<segment>
		<index>29</index>
		<field>PO1</field>
		<field>6</field>
		<field>696</field>
		<field>EA</field>
		<field>9.55</field>
		<field>TE</field>
		<field>CB</field>
		<field>067504-118</field>
		<field>PR</field>
		<field>RO</field>
		<field>VN</field>
		<field>DX1875</field>
	</segment>
	<segment>
		<index>30</index>
		<field>PID</field>
		<field>F</field>
		<field>0null</field>
		<field>0null</field>
		<field>0null</field>
		<field>ORANGE WIDGET</field>
	</segment>
	<segment>
		<index>31</index>
		<field>PO4</field>
		<field>6</field>
		<field>6</field>
		<field>EA</field>
		<field>PLT94</field>
		<field>0null</field>
		<field>3</field>
		<field>LR</field>
		<field>10</field>
		<field>CT</field>
	</segment>
	<segment>
		<index>32</index>
		<field>CTT</field>
		<field>6</field>
	</segment>
	<segment>
		<index>33</index>
		<field>AMT</field>
		<field>1</field>
		<field>13045.94</field>
	</segment>
	<segment>
		<index>34</index>
		<field>SE</field>
		<field>33</field>
		<field>000000010</field>
	</segment>
	<segment>
		<index>35</index>
		<field>GE</field>
		<field>1</field>
		<field>1421</field>
	</segment>
	<segment>
		<index>36</index>
		<field>IEA</field>
		<field>1</field>
		<field>000003438</field>
	</segment>
</holder>
```

After Workato applies the transformation, the output XML follows the structure defined in the XSLT script:

Transformation output

```xml
<?xml version="1.0"?>
<EDI850>
  <ISA>
    <AuthorizationInformationQualifier>01</AuthorizationInformationQualifier>
    <AuthorizationInformation>0000000000</AuthorizationInformation>
    <SecurityInformationQualifier>01</SecurityInformationQualifier>
    <SecurityInformation>0000000000</SecurityInformation>
    <InterchangeIdQualifier_Sender>ZZ</InterchangeIdQualifier_Sender>
    <InterchangeSenderId>ABCDEFGHIJKLMNO</InterchangeSenderId>
    <InterchangeIdQualifier_Receiver>ZZ</InterchangeIdQualifier_Receiver>
    <InterchangeReceiverId>123456789012345</InterchangeReceiverId>
    <InterchangeDate>101127</InterchangeDate>
    <InterchangeTime>1719</InterchangeTime>
    <InterchangeControlVersion>U</InterchangeControlVersion>
    <InterchangeControlStandardsIdentifier>00400</InterchangeControlStandardsIdentifier>
    <InterchangeControlNumber>000003438</InterchangeControlNumber>
    <AcknowledgementRequested>0</AcknowledgementRequested>
    <UsageIndicator>P</UsageIndicator>
  </ISA>
  <GS>
    <FunctionalIdentifierCode>PO</FunctionalIdentifierCode>
    <ApplicationSenderCode>4405197800</ApplicationSenderCode>
    <ApplicationReceiverCode>999999999</ApplicationReceiverCode>
    <Date>20101127</Date>
    <Time>1719</Time>
    <GroupControlNumber>1421</GroupControlNumber>
    <ResponsibleAgencyCode>X</ResponsibleAgencyCode>
    <VersionReleaseIndustryIdentifierCode>004010VICS</VersionReleaseIndustryIdentifierCode>
  </GS>
  <ST>
    <TransactionSetIdentifierCode>850</TransactionSetIdentifierCode>
    <TransactionSetControlNumber>000000010</TransactionSetControlNumber>
  </ST>
  <BEG>
    <TransactionSetPurposeCode>00</TransactionSetPurposeCode>
    <PurchaseOrderTypeCode>SA</PurchaseOrderTypeCode>
    <PurchaseOrderNumber>08292233294</PurchaseOrderNumber>
    <ReleaseNumber>0null</ReleaseNumber>
    <PurchaseOrderDate>20101127</PurchaseOrderDate>
    <ContactNumber>610385385</ContactNumber>
  </BEG>
  <ITD>
    <TermsTypeCode>14</TermsTypeCode>
    <TermsBasisDateCode>3</TermsBasisDateCode>
    <TermsDiscountPercent>2</TermsDiscountPercent>
    <TermsDiscountDueDays>0null</TermsDiscountDueDays>
    <TermsNetDays>45</TermsNetDays>
    <Description>0null</Description>
    <DayOfMonth>46</DayOfMonth>
  </ITD>
  <DTM>
    <DateTimeQualifier>002</DateTimeQualifier>
    <Date>20101214</Date>
  </DTM>
  <PKG>
    <ItemDescriptionType>F</ItemDescriptionType>
    <PackagingCharacteristicCode>68</PackagingCharacteristicCode>
    <Description>0null</Description>
  </PKG>
  <PKG>
    <ItemDescriptionType>F</ItemDescriptionType>
    <PackagingCharacteristicCode>66</PackagingCharacteristicCode>
    <Description>0null</Description>
  </PKG>
  <TD5>
    <RoutingSequenceCode>A</RoutingSequenceCode>
    <IdentificationCodeQualifier>92</IdentificationCodeQualifier>
    <IdentificationCode>P3</IdentificationCode>
    <TransportationMethodTypeCode>SEE XYZ RETAIL ROUTING GUIDE</TransportationMethodTypeCode>
  </TD5>
  <N1>
    <EntityIdentifierCode>ST</EntityIdentifierCode>
    <Name>XYZ RETAIL</Name>
    <IdentificationCodeQualifier>9</IdentificationCodeQualifier>
    <IdentificationCode>0003947268292</IdentificationCode>
  </N1>
  <N3>
    <AddressInformation>31875 SOLON RD</AddressInformation>
  </N3>
  <N4>
    <CityName>SOLON</CityName>
    <StateOrProvinceCode>OH</StateOrProvinceCode>
    <PostalCode>44139</PostalCode>
  </N4>
  <POGroup>
    <PO1>
      <LineNumber>1</LineNumber>
      <Quantity>120</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>9.25</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>SMALL WIDGET</Description>
    </PID>
    <PO4>
      <Pack>4</Pack>
      <Size>4</Size>
      <UOM>EA</UOM>
      <PackagingCode>PLT94</PackagingCode>
      <Weight>0null</Weight>
      <WeightQualifier>3</WeightQualifier>
      <Volume>LR</Volume>
      <VolumeQualifier>15</VolumeQualifier>
    </PO4>
  </POGroup>
  <POGroup>
    <PO1>
      <LineNumber>2</LineNumber>
      <Quantity>220</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>13.79</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>MEDIUM WIDGET</Description>
    </PID>
    <PO4>
      <Pack>2</Pack>
      <Size>2</Size>
      <UOM>EA</UOM>
      <PackagingCode/>
      <Weight/>
      <WeightQualifier/>
      <Volume/>
      <VolumeQualifier/>
    </PO4>
  </POGroup>
  <POGroup>
    <PO1>
      <LineNumber>3</LineNumber>
      <Quantity>126</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>10.99</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>LARGE WIDGET</Description>
    </PID>
    <PO4>
      <Pack>6</Pack>
      <Size>1</Size>
      <UOM>EA</UOM>
      <PackagingCode>PLT94</PackagingCode>
      <Weight>0null</Weight>
      <WeightQualifier>3</WeightQualifier>
      <Volume>LR</Volume>
      <VolumeQualifier>12</VolumeQualifier>
    </PO4>
  </POGroup>
  <POGroup>
    <PO1>
      <LineNumber>4</LineNumber>
      <Quantity>76</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>4.35</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>NANO WIDGET</Description>
    </PID>
    <PO4>
      <Pack>4</Pack>
      <Size>4</Size>
      <UOM>EA</UOM>
      <PackagingCode>PLT94</PackagingCode>
      <Weight>0null</Weight>
      <WeightQualifier>6</WeightQualifier>
      <Volume>LR</Volume>
      <VolumeQualifier>19</VolumeQualifier>
    </PO4>
  </POGroup>
  <POGroup>
    <PO1>
      <LineNumber>5</LineNumber>
      <Quantity>72</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>7.5</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>BLUE WIDGET</Description>
    </PID>
    <PO4>
      <Pack>4</Pack>
      <Size>4</Size>
      <UOM>EA</UOM>
      <PackagingCode/>
      <Weight/>
      <WeightQualifier/>
      <Volume/>
      <VolumeQualifier/>
    </PO4>
  </POGroup>
  <POGroup>
    <PO1>
      <LineNumber>6</LineNumber>
      <Quantity>696</Quantity>
      <UnitOfMeasurement>EA</UnitOfMeasurement>
      <UnitPrice>9.55</UnitPrice>
      <BasisOfUnitPriceCode>TE</BasisOfUnitPriceCode>
      <ProductServiceId>CB</ProductServiceId>
    </PO1>
    <PID>
      <ItemDescriptionType>F</ItemDescriptionType>
      <Description>ORANGE WIDGET</Description>
    </PID>
    <PO4>
      <Pack>6</Pack>
      <Size>6</Size>
      <UOM>EA</UOM>
      <PackagingCode>PLT94</PackagingCode>
      <Weight>0null</Weight>
      <WeightQualifier>3</WeightQualifier>
      <Volume>LR</Volume>
      <VolumeQualifier>10</VolumeQualifier>
    </PO4>
  </POGroup>
  <CTT>
    <NumberofLineItems>6</NumberofLineItems>
  </CTT>
  <AMT>
    <AmountQualifierCode>1</AmountQualifierCode>
    <MonetaryAmount>13045.94</MonetaryAmount>
  </AMT>
  <SE>
    <NumberOfIncludedSegments>33</NumberOfIncludedSegments>
    <TransactionSetControlNumber>000000010</TransactionSetControlNumber>
  </SE>
  <GE>
    <NumberOfTransactionSetsIncluded>1</NumberOfTransactionSetsIncluded>
    <GroupControlNumber>1421</GroupControlNumber>
  </GE>
  <IEA>
    <NumberOfIncludedGroups>1</NumberOfIncludedGroups>
    <InterchangeControlNumber>000003438</InterchangeControlNumber>
  </IEA>
</EDI850>
```

You can parse the transformed XML by using the [Parse XML document action](/en/features/parse-xml-action), which extracts individual datapills for use in recipes. The following datatree represents the structured output:

Output datatree

```text
. EDI 850
  ├── ISA
  |   ├── Authorization information qualifier
  |   ├── Authorization information
  |   ├── Security information qualifier
  |   ├── Security information
  |   ├── Interchange ID qualifier sender
  |   ├── Interchange sender ID
  |   ├── Interchange ID qualifier receiver
  |   ├── Interchange receiver ID
  |   ├── Interchange date
  |   ├── Interchange time
  |   ├── Interchange control version
  |   ├── Interchange control standards identifier
  |   ├── Interchange control number
  |   ├── Acknowledgement requested
  |   └── Usage indicator
  ├── GS
  |   ├── Functional identifier code
  |   ├── Application sender code
  |   ├── Application receiver code
  |   ├── Date
  |   ├── Time
  |   ├── Group control number
  |   ├── Responsible agency code
  |   └── Version release industry identifier code
  ├── ST
  |   ├── Transaction set identifier code
  |   └── Transaction set control number
  ├── BEG
  |   ├── Transaction set purpose code
  |   ├── Purchase order type code
  |   ├── Purchase order number
  |   ├── Release number
  |   ├── Purchase order date
  |   └── Contact number
  ├── ITD
  |   ├── Terms type code
  |   ├── Terms basis date code
  |   ├── Terms discount percent
  |   ├── Terms discount due days
  |   ├── Terms net days
  |   ├── Description
  |   └── Day of month
  ├── DTM
  |   ├── Date time qualifier
  |   └── Date
  ├── PKG
  |   └── List
  |       ├── Item description type
  |       ├── Packaging characteristic code
  |       └── Description
  ├── TD 5
  |   ├── Routing sequence code
  |   ├── Identification code qualifier
  |   ├── Identification code
  |   └── Transportation method type code
  ├── N 1
  |   ├── Entity identifier code
  |   ├── Name
  |   ├── Identification code qualifier
  |   └── Identification code
  ├── N 3
  |   └── Address information
  ├── N 4
  |   ├── City name
  |   ├── State or province code
  |   └── Postal code
  ├── PO Group
  |   └── List
  |       ├── PO 1
  |       |   ├── Line number
  |       |   ├── Quantity
  |       |   ├── Unit of measurement
  |       |   ├── Unit price
  |       |   ├── Basis of unit price code
  |       |   └── Product service ID
  |       ├── PID
  |       |   ├── Item description type
  |       |   └── Description
  |       └── PO 4
  |           ├── Pack
  |           ├── Size
  |           ├── UOM
  |           ├── Packaging code
  |           ├── Weight
  |           ├── Weight qualifier
  |           ├── Volume
  |           └── Volume qualifier
  ├── CTT
  |   └── Numberof line items
  ├── AMT
  |   ├── Amount qualifier code
  |   └── Monetary amount
  ├── SE
  |   ├── Number of included segments
  |   └── Transaction set control number
  ├── GE
  |   ├── Number of transaction sets included
  |   └── Group control number
  └── IEA
      ├── Number of included groups
      └── Interchange control number
```

---
