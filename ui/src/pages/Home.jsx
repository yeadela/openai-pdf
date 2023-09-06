import React from 'react';
import { TabContext, TabList, TabPanel } from '@mui/lab';
import { Tab } from '@mui/material';
import Box from "@mui/material/Box";
import Summary from './Summary';
import HomePage from './HomePage';

export default function Home() {
    const [value, setValue] = React.useState('1');

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return (
        <Box sx={{ width: '100%', typography: 'body1' }}>
            <TabContext value={value}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <TabList onChange={handleChange} aria-label="lab API tabs example">
                        <Tab label="Upload & Summary" value="1" />
                        <Tab label="Ask" value="2" />
                    </TabList>
                </Box>
                <TabPanel value="1"><Summary /></TabPanel>
                <TabPanel value="2"><HomePage /></TabPanel>
            </TabContext>
        </Box>
    );
}

