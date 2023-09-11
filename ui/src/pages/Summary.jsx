import { Button } from '@mui/material'
import React, { useState } from 'react'
import { summaryCompletion } from "../api/chat.api";
import { toast } from "react-toastify";
import { Box } from "@mui/material";

export default function Summary() {
    const [summry, setSummary] = useState("");
    const createSummary = async () => {
        const { response, err } = await summaryCompletion({ prompt: "" });
        if (response) {
            setSummary(response.data);
        }
        if (err) {
            toast.error(err.message);
        }
    }

    return (
        <div>
            <Button onClick={createSummary}>Create Summary</Button>
            <div style={{
                border: "1px solid #ddd",
                width: "600px",
                height: "200px",
                overflow: "auto"
            }}>{summry}</div>
        </div>

    )
}
