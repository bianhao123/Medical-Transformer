paths = 'E:\download\MoNuSegTestData\*.xml';
s = dir(paths);
% for i = 1:1
for i = 1:length(s)
    xml_name = s(i).name(1:23);
    display(xml_name);
    he_to_binary_mask(xml_name);
end