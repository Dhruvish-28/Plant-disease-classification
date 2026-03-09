'use client';

import React, { useRef, useState } from 'react';
import { Upload, AlertCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

interface ImageUploadSectionProps {
  onClassify: (file: File) => void;
  loading: boolean;
}

export default function ImageUploadSection({
  onClassify,
  loading,
}: ImageUploadSectionProps) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const dropZoneRef = useRef<HTMLDivElement>(null);
  const [dragActive, setDragActive] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const ALLOWED_TYPES = ['image/png', 'image/jpeg', 'image/gif'];
  const MAX_FILE_SIZE = 16 * 1024 * 1024; // 16MB

  const validateFile = (file: File): boolean => {
    if (!ALLOWED_TYPES.includes(file.type)) {
      setError('Invalid file type. Please upload PNG, JPG, or GIF.');
      return false;
    }

    if (file.size > MAX_FILE_SIZE) {
      setError('File is too large. Maximum size is 16MB.');
      return false;
    }

    setError(null);
    return true;
  };

  const handleFileSelect = (file: File) => {
    if (validateFile(file)) {
      onClassify(file);
    }
  };

  const handleClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      handleFileSelect(e.target.files[0]);
    }
  };

  const handleDrag = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files?.[0]) {
      handleFileSelect(e.dataTransfer.files[0]);
    }
  };

  return (
    <Card className="flex flex-col gap-6 border-2 border-border bg-card p-8">
      <div className="mb-2">
        <h2 className="text-2xl font-bold text-primary">Step 1: Upload Image</h2>
        <p className="mt-1 text-sm text-muted-foreground">
          Upload a clear photo of a plant leaf
        </p>
      </div>

      {/* Drop Zone */}
      <div
        ref={dropZoneRef}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={handleClick}
        className={`flex cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed p-12 transition-all ${
          dragActive
            ? 'border-accent bg-accent/5'
            : 'border-border bg-secondary/30 hover:bg-secondary/50'
        }`}
      >
        <Upload className="mb-3 h-12 w-12 text-accent" />
        <p className="text-center text-lg font-semibold text-primary">
          Drag and drop your image here
        </p>
        <p className="mt-1 text-center text-sm text-muted-foreground">
          or click to browse
        </p>
      </div>

      {/* Hidden File Input */}
      <input
        ref={fileInputRef}
        type="file"
        accept=".png,.jpg,.jpeg,.gif"
        onChange={handleFileInput}
        className="hidden"
        disabled={loading}
      />

      {/* Error Message */}
      {error && (
        <div className="flex items-center gap-2 rounded-lg bg-destructive/10 p-3 text-destructive">
          <AlertCircle className="h-5 w-5 flex-shrink-0" />
          <p className="text-sm">{error}</p>
        </div>
      )}

      {/* Button */}
      <Button
        onClick={handleClick}
        disabled={loading}
        className="w-full bg-accent py-6 text-base font-semibold text-accent-foreground hover:bg-accent/90 disabled:opacity-50"
      >
        {loading ? 'Classifying...' : 'Select Image'}
      </Button>

      {/* Help Text */}
      <div className="rounded-lg bg-secondary/50 p-4">
        <p className="text-xs text-muted-foreground">
          <span className="font-semibold">Tip:</span> For best results, use clear,
          well-lit photos of plant leaves with visible disease symptoms. Supported
          formats: PNG, JPG, GIF (max 16MB)
        </p>
      </div>
    </Card>
  );
}
