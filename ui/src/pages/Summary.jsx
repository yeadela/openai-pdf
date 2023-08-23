import { Button } from '@mui/material'
import React, { useState } from 'react'
import { summaryCompletion } from "../api/chat.api";
import { toast } from "react-toastify";

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
            <div>{summry}</div>
        </div>

    )
}
